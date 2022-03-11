export function renderPosts(posts) {
    let html = ''
    posts.forEach((post) => {
        html += `
    <a href="/posts/post/${post.code}" class="box" slug="${post.code}" id="box-post">
        <div class="box-body center-c">
            <img src="${post.img}" alt="post-img" class="box-img">
            <h2 class="post-title">${post.title}</h2>
            <p class="box-description">${post.description}</p>
            <div class="box-info sb-x">
                <span class="post-category">${post.category}</span>
                <span class="post-date">${post.date}</span>
            </div>
        </div>
    </a>
        `
    })
    return html
}