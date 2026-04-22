

ToriloShop Product Pages
This project builds full product listing pages for ToriloShop using Django Template Language (DTL) and Bootstrap.

Features
Product List View

Queries all products and renders them in a template.

Uses a for loop to display product details.

Product Detail View

Displays a single product’s name, price, stock status, and category.

Category List View

Shows all categories with a count of products in each.

Templates
base.html

Includes a navbar with links: Home, Products, About.

Footer section for consistent layout.

Extending Templates

All views extend base.html using {% extends %} and {% block %}.

Dynamic Rendering

Loops through products with DTL.

Displays In Stock / Out of Stock badges using {% if %}.

Styling
Basic styling with Bootstrap CDN or inline CSS for quick setup.