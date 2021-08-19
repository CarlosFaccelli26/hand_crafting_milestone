from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from .models import Product, Category, ProductReview, WishList, WishListItem
from .forms import ProductForm, ProductReviewForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    form = ProductReviewForm()
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    reviews = ProductReview.objects.filter(product=product_id)
    paginator = Paginator(reviews, 3)  # Show 3 reviews per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
        'page_obj': page_obj,
    }

    return render(request, 'products/product_detail.html', context)


def review(request, product_id):
    """A view to give user the ability to write a review for a product"""
    
    product = Product.objects.get(pk=product_id)
    reviews = ProductReview.objects.filter(product=product_id)
    user_review = ProductReview.objects.filter(user=request.user)
    user = request.user
    if request.method == 'POST':
        #  Check if username has review on certain product
        if user_review:
            messages.error(request, "You already review this product.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:    
            form = ProductReviewForm(request.POST)
            if form.is_valid():
                review = form.save()
                review.user = user
                review.product = product
                review.save()
                messages.success(request, 'Review Posted.')
                return redirect(reverse('product_detail', args=[product.id]))
            else:
                messages.error(request, 'Failed to post review. Please check the form is valid.')
                return redirect(reverse('product_detail', args=[product.id]))
    else:
        form = ProductReviewForm()

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def delete_review(request, productreview_id):
    """Delete review. Only avaialable to store owners"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    review = get_object_or_404(ProductReview, pk=productreview_id)
    if review:
        review.delete()
        messages.success(request, 'Review Deleted.')
        return redirect(reverse('products'))



@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, __ = WishList.objects.get_or_create(
        user=request.user
    )

    product_wish = WishList.objects.get(user=request.user)
    products_count = product_wish.products.all()

    if product in products_count:
        messages.error(request, 'Already in Wishlist.')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        wishlist.products.add(product)
        print(product)
        messages.success(request, 'Added to Wishlist.')
        return redirect(reverse('wishlist'))


@login_required
def wishlist(request):
    wishlist_list = WishList.objects.get(
        user=request.user
        )
    wishlist_count = wishlist_list.products.all()
    paginator = Paginator(wishlist_count, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'wishlist_list': wishlist_list,
        'wishlist_count': wishlist_count,
        'page_obj': page_obj,
    }
    return render(request, 'products/wishlist.html', context)


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, __ = WishList.objects.get_or_create(
        user=request.user
    )

    wishlist.products.remove(product)
    messages.success(request, 'Removed from Wishlist.')
    return redirect('wishlist')


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product Added.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are edting {product.name}')
    
    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted.')
    return redirect(reverse('products'))
