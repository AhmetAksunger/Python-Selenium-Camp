
# SauceDemo All Actions Test

Testing all the actions I find in www.saucedemo.com for the second homework in Python Selenium Camp

## Test Images
Note: one of the test_img_sources test was given False on purpose, to show that the tests catches if the images are same.
![test_results](https://user-images.githubusercontent.com/116587797/228530709-32dd6bf6-c928-4395-9dd8-e10a49df1fa0.png)

## Test Screenshots Preview
![Screenshot_4](https://user-images.githubusercontent.com/116587797/228530957-13d376dc-0626-4446-aef1-6c71f7fab39a.png)


## test_empty_username
Tests the case where the username and password are empty, and the case where the username is empty, but the password is not.

## test_empty_password
Tests the case where the password is empty, and the username is not.

## test_locked_out_user
Tests the case where the user is locked out

## test_valid_login
tests the case where the user provides valid login infos and logs in successfully.

## test_product_count
tests whether the number of products when we add them all to the cart matches the expected number of products.

## test_error_icon
tests whether the error icon is properly displayed when an error occurs on and undisplayed when the x button is clicked.

## test_add_to_cart
tests whether the "Add to Cart" button is working simultanouly with the shopping cart icon. Checks if the shopping cart icon's text is changing depending on the add to cart button

## test_shopping_cart
tests whether the items that are added to cart is on the carts section

## test_total_amount
tests whether the total amount in the payment section is true or not

## test_img_sources
tests whether all the images in the inventory list has the same img or not

## test_empty_first_name_checkout
tests the Empty first name error in the checkout section

## test_za_filter
tests Name(Z to A) filter in the inventory list

## test_lohi_filter
tests Price(low to high) filter in the inventory list

## test_holi_filter
tests Price(high to low) filter in the inventory list

## test_logout
tests the log out button
