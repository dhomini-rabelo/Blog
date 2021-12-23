function asyncPost(url, body) {
    return fetch(url,{
        method: "POST",
        headers: {
            "Content-Type": "text/plain",
        },
        body: JSON.stringify(body)
    }).then((data)=>data.json())
 
}