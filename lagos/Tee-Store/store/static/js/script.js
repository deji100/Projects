const category = document.getElementById('category');
const links = document.getElementById('category-links');
category.onclick = viewLinks
links.onmouseleave = closeLinks

function viewLinks() {
    const cat_links = document.getElementById('category-links');
    cat_links.style.visibility = 'visible';
}

function closeLinks() {
    const cat_links = document.getElementById('category-links');
    cat_links.style.visibility = 'hidden';
}
