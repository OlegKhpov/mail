document.addEventListener('DOMContentLoaded', function () {
  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector("#compose-form").onsubmit = () => {
    let email = {
      recipients: document.querySelector('#compose-recipients').value,
      subject: document.querySelector('#compose-subject').value,
      body: document.querySelector('#compose-body').value,
    }
  
    fetch(`/emails`, {
      method: 'POST',
      mode: "cors",
      headers: {
        'Content-Type': 'application/json;charset=utf-8'
      },
      body: JSON.stringify(email)
    })
    .then(result => {      
      load_mailbox('sent')      
    })
    .catch(e => console.log(e))
    return false
  }


  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email(to = null) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#emails-list').style.display = 'none';
  document.querySelector('#single-view').style.display = 'none';



  // Clear out composition fields
  if (typeof to === 'number') {
    fetch(`/emails/${to}`)
      .then(response => response.json())
      .then(result => {
        document.querySelector('#compose-recipients').value = `${result['sender']}`;
        document.querySelector('#compose-subject').value = 'Re:';
        document.querySelector('#compose-body').value = `At ${result['timestamp']}, ${result['sender']} wrote: ${result['body']}`;
      })
  } else {
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
  }
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-list').style.display = 'block';
  document.querySelector('#single-view').style.display = 'none';

  fetch(`/emails/${mailbox}`, {
    method: "GET"
  })
    .then(response => {
      return response.json()
    })
    .then(result => {
      let element = document.querySelector('#emails-list')
      element.innerHTML = ''
      for (let i = 0; i < result.length; i++) {
        let msg = result[i]
        if (mailbox === 'archive') {
          element.innerHTML += `<li class="list-group-item">
              <div class="btn-group w-100" role="group" aria-label="Basic example">
                  <button id="one-email" type="button" class="btn btn-secondary text-left" style="width: 80%;" onclick="show_email(${msg['id']})">from: <b>${msg['sender']}</b> subject: <b>${msg['subject']}</b> date: <b>${msg['timestamp']}</b></button>
                  <button type="button" class="btn btn-secondary" style="width: 10%;" onclick="unarchive(${msg['id']})">Unarchive</button>
                  <button type="button" class="btn btn-danger" style="width: 10%;">Delete</button>                
                  </div>
                </li>`
        } else if (mailbox === 'sent') {
          element.innerHTML += `<li class="list-group-item">
            <div class="btn-group w-100" role="group" aria-label="Basic example">
                <button id="one-email" type="button" class="btn btn-light text-left" style="width: 100%;" onclick="show_email(${msg['id']})">to: <b>${msg['recipients']}</b> subject: <b>${msg['subject']}</b> date: <b>${msg['timestamp']}</b></button>
            </div>
          </li>`
        } else {
          if (msg['read']) {
            element.innerHTML += `<li class="list-group-item">
            <div class="btn-group w-100" role="group" aria-label="Basic example">
                <button id="one-email" type="button" class="btn btn-secondary text-left" style="width: 80%;" onclick="show_email(${msg['id']})">from: <b>${msg['sender']}</b> subject: <b>${msg['subject']}</b> date: <b>${msg['timestamp']}</b></button>
                <button type="button" class="btn btn-secondary" style="width: 10%;" onclick="archive(${msg['id']})">Archive</button>
                <button type="button" class="btn btn-danger" style="width: 10%;" onclick="unread(${msg['id']})">Unread</button>                
                </div>
              </li>`
          } else if (!msg['read']) {
            element.innerHTML += `<li class="list-group-item">
              <div class="btn-group w-100" role="group" aria-label="Basic example">
                  <button id="one-email" type="button" class="btn btn-outline-secondary text-left" style="width: 80%;" onclick="show_email(${msg['id']})">from: <b>${msg['sender']}</b> subject: <b>${msg['subject']}</b> date: <b>${msg['timestamp']}</b></button>
                  <button type="button" class="btn btn-secondary" style="width: 10%;" onclick="archive(${msg['id']})">Archive</button>
                  <button type="button" class="btn btn-danger" style="width: 10%;" onclick="read(${msg['id']})">Read</button>                 
                  </div>
                </li>`
          }
        }
      }
    })
    .catch(e => console.log(e))

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
}

function show_email(id) {
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-list').style.display = 'none';
  document.querySelector('#single-view').style.display = 'block';



  let element = document.querySelector('#emails-view')
  element.innerHTML = `<h3>Email</h3>`;
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  })
  fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(result => {
      let to_list = result['recipients'].join(', ')
      element.innerHTML += `
      <div>
        <ul class="list-group">
            <li class="list-group-item">from: ${result['sender']}</li>
            <li class="list-group-item">to: ${to_list}</li>
            <li class="list-group-item">date: ${result['timestamp']}</li>
          </ul>
        <p>subject: <b>${result['subject']}</b></p>
        <p>${result['body']}</p>
        <button type="button" class="btn btn-danger" onclick="compose_email(${result['id']})">Reply</button>
      </div>`
    });
};

function archive(id) {
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      archived: true
    })
  });
};

function unarchive(id) {
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      archived: false
    })
  });
};

function read(id) {
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  });
};

function unread(id) {
  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: false
    })
  });
};