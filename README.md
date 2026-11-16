# Django URL Routing Practice

A simple Django application demonstrating basic URL routing using `path()` and path converters (`int`, `slug`).

## Project Files
* `urls.py` — URL patterns configuration for the app.
* `views.py` — View functions returning `HttpResponse`.

## Routes
* `/` — Home page
* `/posts/<int:post_id>/` — View post by integer ID (e.g., `/posts/1/`)
* `/posts/<slug:post_slug>/` — View post by string slug (e.g., `/posts/first-post/`)
