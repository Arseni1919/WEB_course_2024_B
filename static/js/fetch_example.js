

const execute_get_fetch  = (e) => {
    e.preventDefault()

    fetch(
            '/fetch_example'
    ).then(
            res => res.json()
    ).then(
            (res) => {
                console.log(res)
                const res_str = JSON.stringify(res)
                const title2 = document.querySelector('.title2')
                title2.innerHTML = `${res_str}`
            }

    ).catch(err => console.log(err))

    // fetch('/fetch_example').then(
    //         response => response.json()
    // ).then(
    //         (responseJSON) => {
    //             const res = JSON.stringify(responseJSON)
    //             const title2 = document.querySelector('.title2')
    //             title2.innerHTML = `${res}`
    //             console.log(res)
    //         }
    //
    // ).catch(
    //         err => {
    //             console.log(err)
    //             const title2 = document.querySelector('.title2')
    //             title2.innerHTML = `NOPE`
    //         }
    // );
}

const myForm = document.querySelector('#my-form-get');
myForm.addEventListener('submit', execute_get_fetch);


const execute_post_fetch = (e) => {
    e.preventDefault()

    // prepare data
    data = {'a': 1, 'b': 2}

    fetch('/fetch_example', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    }
    ).then(
            response => response.json()
    ).then(
            (responseJSON) => {
                const res = JSON.stringify(responseJSON)
                console.log(res)
                const title3 = document.querySelector('.title3')
                title3.innerHTML = `${res}`
            }
    ).catch(
            err => console.log(err)
    );
}


const myFormPost = document.querySelector('#my-form-post');
myFormPost.addEventListener('submit', execute_post_fetch);
