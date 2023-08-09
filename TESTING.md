### Return to README.md

[README.md](https://github.com/MattyOL/Fresh-Vintage-P5-/blob/main/README.md)
## Code Validation
I have used the recommended HTML W3C Validator to validate all of my HTML files.

In order to properly validate my HTML pages with Jinja syntax for authenticated pages, I followed these steps:

* Navigate to the deployed pages which require authentication
* Right-click anywhere on the page, and select View Page Source (usually CTRL+U or ⌘+U on Mac).
* This will display the entire "compiled" code, without any Jinja syntax.
* Copy everything, and use the validate by input method.
* Repeat this process for every page that requires a user to be logged-in/authenticated

### Home-page 


|   Page        |    Url        | Screenshot  | Results   |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
|    Home       |  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
|    Sign In    |  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
|    Logout     |  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
|  All product's|  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
|    Homewear   |  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
|    Clothing   |  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
|    Blog       |  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
|Special Offer  |  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
|    WIshlist   |  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
| Product manage|  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
|  Contac       |  [W3C]()      |             |   Pass    |
|               |               |             |           |
|               |               |             |           |
| ------------- |   ---------   | -----------:|----------:|
|               |               |             |           |
| My profile    |  [W3C]()      |             |   Pass    |
|               |               |             |           |






* no issues 



### Login 
* no issues 



### Contact form 
* no issues 




### wishlist
* no issues 



### 404 error page
* no issues 


## Css Testing 
* I have used the recommended CSS Jigsaw Validator to validate my CSS file. 
* No issues 

## Python 
I have used the recommended CI Python Linter to validate all of my Python files.

## tests.py 
I done some test's in the test.py file using the terminal to get results using the 
* python3 manage.py test / command 
 

### Results 

## Manual Testing 
1. * Test: click on Login button.
   * Expected result: taken to login screen.
   * Result: pass.

2. * Test:click on Sign up form.
   * Expected: taken too signup form Create an account.
   * Result: pass.

3. * Test: Home button navbar.
   * Expected: taken to home page.
   * Results: pass.

4. * Test:Click Contact form.
   * Expected:to be brought to page, form filled out, submit.
   * Result: pass.



6. * Test:Search bar searches products.
   * Expected: To be displayed with products.
   * Result: pass.
   
7. * Test: Search invalid entry to display 404 error.
   * Expected: To be brought to 404error feedback.
   * Result: pass.

8. * Test: Go back button on 404page.
   * Expected: to return to home.
   * Result: pass.

9. * Test: Logout.
   * Expected: user to logout.
   * Result: pass.

10. * Test: When user clicks a blog post.
    * Expected: To be brought into the posts info.
    * Results: pass.
11. *

12. * 

13. * 

13. * Test: likes/comments on posts.
    * Expected: The admin has to verify like/comments on post when submitted.
    * Results: pass.

14. * Test: websites name is clickable.
    * Expected: to refresh to home-page.
    * Results: pass.

15. * Test: if contact form gets sent to admin.
    * Expected: admin gets email sent from contact for filled by user. 
    * Results: pass.

16. * Test: User cannot delete a post they didnt create.
    * Expected: To be not aloud to delete a post they did not create. 
    * Results: pass.

17. * Test: When a user is not signed in can they view the contact/wishlist/ form. 
    * Expected: Not to be able to see the contact/add recipe form.
    * Results: pass.
## linter pylint 
I used linter pylint to test the python code.
* No major issues to be found.


## Responsiveness

* I am pleased to inform you that the website you are using is fully responsive, ensuring a seamless user experience across all devices. Whether you access the website from a desktop computer, laptop, tablet, or smartphone, its layout, design, and functionality adapt flawlessly to different screen sizes and resolutions. This responsiveness guarantees that you can enjoy the website's features, navigate effortlessly, and interact with its content efficiently, regardless of the device you choose to use. With a commitment to providing an optimal user experience, the website's responsiveness ensures accessibility and convenience for all visitors, enhancing your satisfaction and usability.

Results = pass fully responsive


## Lighthouse Test's

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

### Home page

* Desktop devices

* Mobile devices



### About page

* Desktop devices


* Mobile devices



### Sign up page

* Desktop devices


* Mobile devices


### Login page

* Desktop devices


* Mobile devices


### Contact Form

* Desktop devices


* Mobile devices


### 

* Desktop devices


* Mobile devices


### 404 error page

* Desktop devices


* Mobile devics


### Log out page

* Desktop devices


* Mobile devices


