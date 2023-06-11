class Locators:

    # homepage
    page_logo="//h1[@class='logo-font ng-binding']"
    singin_link="//a[@href='#/login']"
    singup_link="//a[@href='#/register']"

    #signunp page

    singup_page_header="//h1[@class='text-xs-center ng-binding']"
    username_input = "//input[@type='text']"
    email_input="//input[@type='email']"
    password_input="//input[@type='password']"
    signup_button="//button[@type='submit']"

    #article page

    signin_home_page="//a[@ui-sref-active='active' and @class='nav-link ng-binding']"
    new_article_link="//a[@ui-sref='app.editor']"
    article_title_input="//input[@placeholder='Article Title']"
    article_about_input="//input[contains(@placeholder,'article about?')]"
    article_description_input="//textarea[@placeholder='Write your article (in markdown)']"
    article_tags_input="//input[@placeholder='Enter tags']"
    publish_article_button="//button[@type='button']"

    #singin page
    signin_email_input="//input[@type='email']"
    signin_password_input="//input[@type='password']"
    singin_button="//button[@type='submit']"

    #comment page
    comment_input="//textarea[contains(@placeholder,'Write a comment')]"
    comment_button="//button[@type='submit']"
    commented_box="//p[@class='card-text ng-binding']"





