const btn = document.querySelector('button')
const form = document.querySelector('form')
const input = document.querySelector('#file')

btn.onclick = (evt) => {
    evt.preventDefault()
    const file = input.files[0]

    console.log(file.name, file.size)
    form.submit()
}