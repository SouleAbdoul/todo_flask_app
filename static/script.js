// add task functionality
let i = 0;
function sendDate(task){
    fetch("http://localhost:5000/login", {
    method: "POST",
    body: JSON.stringify({task_name: task}),
     headers: {
      "Content-type": "application/json"
     }
}).then(
  console.log("data posted")
)
}
async function getData(){
    let new_data ;
    let response = await fetch("http://localhost:5000/login")
    await response.json().then((data)=>new_data = data);
    //console.log(data);
    return new_data;
}
//function getData(){
 //   let data;
  //  fetch("http://localhost:5000/login",{
   //     method:'GET',
    //    headers:{
     //       'Content-type': 'application/json',
      //  }
    //})
    //.then((response) => response.json())
    //.then(console.log(response))
    //.catch((error)=>{
     //   console.log(error);
    //})
    //return data;
//}


function addTask() {
    // get the input field and task list elements
    let taskInput = document.getElementById("new-task");
    let taskList = document.getElementById("incomplete-tasks");
    console.log('taskInputs value: ', taskInput.value);
    
    // check if input field is not empty or contains only whitespace
    if (taskInput.value != "" && taskInput.value.trim() != "") {
        // create a new list item
        let li = document.createElement("li");
        li.id=`list-${i}`
        li.onclick = (()=> deleteTask());

        // add the task text to the list item
        li.appendChild(document.createTextNode(taskInput.value));
        
        // display the list item to the task list
        taskList.appendChild(li);

        sendDate(taskInput.value)
        // clear the input field
        taskInput.value = "";
    }
    i++;
}

 function deleteTask(){
      document.addEventListener('click', async function(e){
        e.preventDefault();
        var t = e.target;
        // First post the todo name in the todo list
        // second when clicked over it should disapear from the list and appear to the completed list
        // 
        console.log(t.innerHTML);
        let my_data = await getData()
          console.log(my_data[0]);
    },false)
    
}
