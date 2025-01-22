// Create header
const header = document.createElement('header');
header.innerHTML = "<h1> Welcome to our website: Crust and Craft </h1>"
document.body.appendChild(header)

// Create a section for three articles

const section = document.createElement('section');

for(var i = 0; i <= 3; i++){
    const article = document.createElement('article')
    const img = document.createElement('img')
    img.src = './images/pizza.jpg';
    const content = document.createElement('p')
    content.innerHTML = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Temporibus dolores in, officia et iusto, consequuntur porro eligendi suscipit quaerat inventore ipsum eaque veniam ex natus?"
    article.appendChild(img);
    article.appendChild(content);
    section.appendChild(article);
}
document.body.appendChild(section);

// Create footer
const footer = document.createElement('footer')
footer.innerHTML = '<p> 2025 Crust and Craft. All Rights Reserved.</p>'
footer.className = 'fsd'
footer.id = 'asdf'
for(var i = 0; i < 2; i++){
    let link = document.createElement('a');
    link.href= 'http://#'
    link.innerHTML = "Click here to"
    footer.appendChild(link)
}
document.body.appendChild(footer);
