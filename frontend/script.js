async function uploadResume(){

let fileInput = document.getElementById("resumeFile")

let formData = new FormData()

formData.append("file", fileInput.files[0])

let response = await fetch("/resume/upload",{
method:"POST",
body:formData
})

let data = await response.json()

document.getElementById("result").textContent =
JSON.stringify(data,null,2)

}


async function askQuestion(){

let question = document.getElementById("question").value

let response = await fetch("/resume/ask?question="+question,{
method:"POST"
})

let data = await response.json()

document.getElementById("answer").textContent =
JSON.stringify(data,null,2)

}