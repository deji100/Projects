const out = function() {
    const buts = document.getElementsByClassName('but');
    for (var i = 0; i < buts.length; i++) {
        buts[i].setAttribute('id', 'b');
    }
}
out()

function form() {
    const inputs = document.getElementsByTagName('input');
    inputs[1].placeholder = 'Username';
    inputs[2].placeholder = 'Gmail';
    inputs[3].placeholder = 'Password';
    inputs[4].placeholder = 'Confirm Password';
    }
form()

function input() {
    const inputs = document.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].setAttribute('class', 'inp');
    }
}
input()

// function addToWatchList() {
//     const addBtns = document.getElementsByClassName('addBtn');

//     for (var i=0; i < addBtns.length; i++) {
//         addBtns[i].addEventListener('click', function() {
//             const listing_id = this.dataset.listing;
//             const action = this.dataset.action;
//             console.log('Listing Id:', listing_id, 'Action:', action)

//             console.log('User:', user)
//             if (user === 'AnonymousUser') {
//                 console.log('User is not authenticated.')
//             }
//             else {
//                 updateUserWatchList(listing_id, action)
//             }
//         })
//     }
// }
// addToWatchList()

// function updateUserWatchList(listing_id, action) {
//     console.log('User is authenticated, sending data...')

//     const url = '/update_listing/'

//     fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken
//         },
//         body: JSON.stringify({
//             'listingId': listing_id,
//             'action': action,
//         })
//     })
//     .then((response) => {
//         return response.json()
//     })

//     .then((data) => {
//         console.log('data:', data);
//         location.reload()
//     })
// }