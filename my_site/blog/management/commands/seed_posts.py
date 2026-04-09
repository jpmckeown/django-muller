from django.core.management.base import BaseCommand
from blog.models import Post
from datetime import date
import textwrap

posts = [
    {
        "slug": "hike-in-the-mountains",
        "image_name": "mountains.jpg",
        "date": date(2026, 3, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": textwrap.dedent(
"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """)
    },
    {
        "slug": "programming-is-fun",
        "image_name": "coding.jpg",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": textwrap.dedent(
"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """)
    },
    {
        "slug": "into-the-woods",
        "image_name": "woods.jpg",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": textwrap.dedent(
"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """)
    }
]

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Post.objects.bulk_create([Post(**p) for p in posts])

        # for p in posts:
        #     Post.objects.get_or_create(slug=p["slug"], defaults=p)
 
