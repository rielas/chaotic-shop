CSS = """
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}
header {
    background: #333;
    color: #fff;
    padding-top: 30px;
    min-height: 70px;
    border-bottom: #77aaff 3px solid;
}
header a {
    color: #fff;
    text-decoration: none;
    text-transform: uppercase;
    font-size: 16px;
}
header ul {
    padding: 0;
    list-style: none;
}
header li {
    float: left;
    display: inline;
    padding: 0 20px 0 20px;
}
header #branding {
    float: left;
}
header #branding h1 {
    margin: 0;
}
header nav {
    float: right;
    margin-top: 10px;
}
#showcase {
    min-height: 400px;
    background: url('showcase.jpg') no-repeat 0 -400px;
    text-align: center;
    color: #fff;
}
#showcase h1 {
    margin-top: 100px;
    font-size: 55px;
    margin-bottom: 10px;
}
#showcase p {
    font-size: 20px;
}
#products, #categories {
    margin: 20px 0;
}
.product, .category {
    background: #fff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.product h2, .category h2 {
    margin-top: 0;
}
.product p, .category p {
    margin: 10px 0;
}
.product a, .category a {
    display: inline-block;
    margin-top: 10px;
    padding: 10px 20px;
    background: #333;
    color: #fff;
    border-radius: 5px;
    text-decoration: none;
}
.product a:hover, .category a:hover {
    background: #77aaff;
}
.sidebar-container {
    float: left;
    width: 20%;
}
.sidebar {
    background: #fff;
    padding: 20px;
    margin-right: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.main-content {
    float: left;
    width: 75%;
}
"""
