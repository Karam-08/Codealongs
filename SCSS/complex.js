const siteData = {
    header: "Welcome to Crust and Craft",
    bannerImage: {
        image: "https://as1.ftcdn.net/jpg/02/34/63/04/1000_F_234630430_48KZrdOyuUeGj9PrjWUVXZHzAfbLn3Ti.jpg",
        alt: "Pizzaria Banner Image"
    }, 
    navLinks:["Home", "About", "Services", "Content"],
    mainContent:[
        {
            title: "Crust and Craft: Make your own Pizza",
            image: "https://www.allrecipes.com/thmb/qZ7LKGV1_RYDCgYGSgfMn40nmks=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/AR-24878-bbq-chicken-pizza-beauty-4x3-39cd80585ad04941914dca4bd82eae3d.jpg",
            description: "Our Pizzeria lets you select the ingredients for your Pizza."
        },{
            title: "Crust and Craft: Chef Made Pizzas",
            image: "https://bakerbynature.com/wp-content/uploads/2015/10/IMG_8476-2-3.jpg",
            description: "Our chefs know a lot about Pizza making, and they know how to make popular Pizzas too. We cater to everyone's prefrence.",
        },{
            title: "Crust and Craft: Frozen Pizzas",
            image: "https://www.simplyrecipes.com/thmb/KE6iMblr3R2Db6oE8HdyVsFSj2A=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__simply_recipes__uploads__2019__09__easy-pepperoni-pizza-lead-3-1024x682-583b275444104ef189d693a64df625da.jpg",
            description: "We also sell our Pizzas as frozen food so that you can store and eat them later."
        }
    ],
    footer: "Crust and Craft 2025. All Rights Reserved."
}

// Create and append elements dynamically

const createAndAppend = (tag, parent, attributes = {}, content = "")=>{
    const element = document.createElement(tag);
    Object.keys(attributes).forEach(key=>element.setAttribute(key,attributes[key]));
    element.innerHTML = content;
    parent.appendChild(element);
    return element;
}

// Create header

const header = createAndAppend("header",document.body,{class:"site-header"})

//Create banner image
const banner = createAndAppend("div",document.body,{class:"site-banner"})
createAndAppend('img', banner,{src:siteData.bannerImage.image, alt:"siteData.bannerImage.alt, width:siteData.bannerImage.width, height:siteData.bannerImage.height"})

//Create Navigation

const nav = createAndAppend("nav", document.body,{class:"site-nav"})
const ul = createAndAppend("ul", nav)

siteData.navLinks.forEach(link=>{
    createAndAppend("li", ul, {}, `<a href="#">${link}</a>`)

})

//Create main content

const main = createAndAppend("main",document.body,{class:"site-main"})

siteData.mainContent.forEach(section =>{
    const article = createAndAppend("article", main,{class: "content-section"})
    createAndAppend("h2",article,{},section.title)
    createAndAppend("img",article,{src:section.image, alt:section.title})
    createAndAppend("p",article,{},section.description)
});

//Create footer

const footer = createAndAppend("footer",document.body,{class:"site-footer"})
createAndAppend("p",footer,{},siteData.footer)

//Create some styling
const style = `
body{ font-family:Arial,sans-serif; margin:0; padding: 0; line-height: 1.6;}
 header{background-color: #333; color: #fff; padding: 1rem; text-align:center;}
 .site-banner img{width: 100%; display:block;}
 nav ul {list-style:none; padding:0; margin:0; display:flex; justify-content:center; background-color: #555;}
 nav ul li{margin: 0 1rem;}
 nav ul li a { color:#fff; text-decoration:none;}
 main:{padding:1rem;}
 .content-section {margin-bottom: 2rem;}
 .content-section img{width:100% height: auto;}
 footer{ background: #333; color: #fff; text-align: center; padding: 1rem; }
`
createAndAppend("style", document.head, {}, style)