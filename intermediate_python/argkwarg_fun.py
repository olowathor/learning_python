'''
blog_1 = 'I am so awesome'
blog_2 = 'Cars are cool'
blog_3 = 'Aww look at my cat!'

site_title = 'My blog'

def blog_posts(title, *args):
    print('Site title: {}'.format(site_title))
    for post in args:
        print(post)
    print('\n\n')

blog_posts(site_title, blog_1, blog_2, blog_3)

def blog_posts_kw(title, **kwargs):
    print('Site title: {}'.format(site_title))
    for p_title,post in kwargs.items():
        print(p_title, post)
    print('\n\n')

blog_posts_kw(site_title, blog_1 = 'I am so awesome',
                            blog_2 = 'Cars are cool',
                            blog_3 = 'Aww look at my cat!')

def blog_posts_arkw(title, *args, **kwargs):
    print('Site title: {}'.format(site_title))
    for arg in args:
        print(arg)    
    for p_title,post in kwargs.items():
        print(p_title, post)

blog_posts_arkw(site_title, blog_1, blog_2, blog_3,
                            blog_1 = 'I am so awesome',
                            blog_2 = 'Cars are cool',
                            blog_3 = 'Aww look at my cat!')
'''
import matplotlib.pyplot as plt

x1 = [1,2,3]
y1 = [2,2,1]

graph_me = [x1,y1]

def graph_operation(x,y):
    print('Graphs: {} and {}'.format(str(x),str(y)))
    plt.plot(x1,y1)
    plt.show()

graph_operation(*graph_me)

