from django.shortcuts import render,get_object_or_404,redirect
from .models import Banner,Product,Category,Blog,Blog_detail,Color
from django.db.models import Q
from app_social.models import Comment,Question
from app_social.forms import CommentForm,QuestionForm,AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app_payment.models import Basket,BasketItem
from app_account.models import Profile,Address

@login_required
def cart(request):
    basket = Basket.objects.filter(user=request.user).first()
    item_count = basket.basketitem_set.count() if basket else 0
    total_price = 0

    # نمایش صفحه سبد خرید خالی در صورت نبودن آیتم
    if item_count == 0:
        return render(request, 'cart-empty.html', {'basket': basket, 'item_count': item_count, 'category': Category.objects.all()})

    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if item_id:
            item = get_object_or_404(BasketItem, id=item_id, basket=basket)
            item.delete()
            return redirect('app_market:cart')

    items = basket.basketitem_set.all() if basket else []
    total_price = sum(item.product.discounted_price() * item.count for item in items)

    context = {
        'basket': basket,
        'items': items,
        'total_price': total_price,
        'item_count': item_count,
        'category': Category.objects.all(),
    }
    return render(request, 'cart.html', context)



def index(request):
    basket = None
    item_count = 0

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).first()
        item_count = basket.basketitem_set.count() if basket else 0

    context = {
        'banner_images': Banner.objects.get(title='index_banner'),
        'products': Product.objects.all(),
        'sugessted_products': Product.objects.filter(is_suggested=True),
        'amazing_products': Product.objects.filter(is_amazing=True),
        'footer_right': Product.objects.filter(footer_right=True),
        'footer_left': Product.objects.filter(footer_left=True),
        'footer_Middle': Product.objects.filter(footer_Middle=True),
        'category': Category.objects.all(),
        'item_count': item_count  
    }
    return render(request, 'index.html', context)


def my_search(request):
    query = request.GET.get('q')
    if query is not None:
        serch_products = Product.objects.filter( Q(name_fa__icontains=query) | Q(name_en__icontains=query) )
    else:
        serch_products = Product.objects.all()
    return render(request, 'search.html', {'serch_products': serch_products})


def product_detail(request, id):
    item_count = 0
    product = get_object_or_404(Product, id=id)
    question_count = Question.objects.filter(product=product).count()
    comments_count = Comment.objects.filter(product=product).count()
    comments = Comment.objects.filter(product=product)
    questions = Question.objects.filter(product=product)
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).first()
        item_count = basket.basketitem_set.count() if basket else 0

    question_form = QuestionForm()

    if request.method == 'POST':
        if 'vote_type' in request.POST:
            comment_id = request.POST.get('comment_id')
            vote_type = request.POST.get('vote_type')
            comment = get_object_or_404(Comment, id=comment_id)

            if vote_type == 'helpful':
                comment.helpful_count += 1
            elif vote_type == 'not_helpful':
                comment.not_helpful_count += 1

            comment.save()
            return redirect('app_market:product_detail', id=product.id)

        elif 'question_text' in request.POST:
            if not request.user.is_authenticated:
                messages.warning(request, "برای ثبت سوال، لطفاً وارد شوید.")
                return redirect('login')
            
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.product = product
                question.user = request.user  
                question.save()
                return redirect('app_market:product_detail', id=product.id)

        elif 'answer_text' in request.POST:
            if not request.user.is_authenticated:
                messages.warning(request, "برای ثبت پاسخ، لطفاً وارد شوید.")
                return redirect('login')
            
            answer_form = AnswerForm(request.POST)
            if answer_form.is_valid():
                question_id = request.POST.get('question_id')  
                question = get_object_or_404(Question, id=question_id)
                
                if not hasattr(question, 'answer'):
                    answer = answer_form.save(commit=False)
                    answer.question = question
                    answer.user = request.user 
                    answer.save()
                return redirect('app_market:product_detail', id=product.id)

    context = {
        'product': product,
        'comments': comments,
        'questions': questions,
        'question_form': question_form,
        'question_count': question_count, 
        'comment_count': comments_count,
        'category': Category.objects.all(),
        'item_count': item_count
    }

    if product.count > 0:
        return render(request, 'product-detail.html', context)
    else:
        return render(request, 'single-product-not-available.html', context)

@login_required       
def product_comment(request, id):
    product = Product.objects.get(id=id)
    comments = Comment.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        positive_points = request.POST.get('positive_points')
        negative_points = request.POST.get('negative_points')

        if not positive_points or not negative_points:
            messages.error(request, 'لطفاً همه مشخصات را پر کنید.')
            form.add_error(None, "لطفاً همه مشخصات را پر کنید.")  
        elif form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('app_market:product_detail', id=product.id)
    else:
        form = CommentForm()

    return render(request, 'product-comment.html', {
        'product': product,
        'comments': comments,
        'form': form,
        'category': Category.objects.all()
    })
        
def blog(request):
    context = {
        'blog':Blog.objects.all(),  
        'category': Category.objects.all()
    }
   
    return render(request, 'blog.html', context)

def blog_detail(request):
     context = {
          'blog_detail':Blog_detail.objects.all(),
          'category': Category.objects.all()
     }
     return render(request,'blog_detail.html',context)

def product_list_by_category(request, category_id):
    main_category= Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(Category=category)
    return render(request, 'product_list.html', {'products_list': products, 'category_list': category , 'category':main_category})

def qaview(request):
    return render(request,'page-faq-category.html')


@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        color_id = request.POST.get('color')
        color = Color.objects.get(id=color_id)

        if request.user.is_authenticated:
            basket = Basket.objects.filter(user=request.user).first()

        if not basket:
            basket = Basket.objects.create(user=request.user)

        BasketItem.objects.create(basket=basket, product=product, color=color, count=1)

    return redirect('app_market:cart')


@login_required
def shopping(request):
    addresses = Address.objects.filter(user=request.user)
    
    basket = Basket.objects.filter(user=request.user).first()
    item_count = basket.basketitem_set.count() if basket else 0
    total_price = 0

    items = basket.basketitem_set.all() if basket else []
    total_price = sum(item.product.discounted_price() * item.count for item in items)
    
    if request.method == "POST":
        messages.warning(request, "سایت متعلق به ارگان یا شاپی نمی‌باشد و امکان ادامه دادن سفارش نیست")

    selected_address_id = request.session.get('selected_address_id')

    context = {
        'addresses': addresses,
        'selected_address_id': selected_address_id,
        'total_price': total_price, 
        'item_count': item_count  
    }
    return render(request, 'shopping.html', context)