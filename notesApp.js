const addBtn = document.querySelector("#addBtn")
const main = document.querySelector("#main")

const saveNote= ()=>{
    const notes=document.querySelector(".note textarea");
    console.log (notes);
    const data=[];
    notes.forEach(
        (note) => {
            data.push(note.value)
        }
    )
}

addBtn.addEventListener(
    "click", function () {
        addNote()
    }
)
//     < div class="note" >
// <div class="tool">
//     <i class=" disk fa-regular fa-floppy-disk"></i>
//     <i class=" trash fa-solid fa-trash"></i>
// </div>

// <textarea></textarea>    
// </ div> 

const addNote = () => {
    const note = document.createElement("div");
    note.classList.add("note")
    note.innerHTML = `
      
    <div class="tool">
        <i class=" disk fa-regular fa-floppy-disk"></i>
        <i class=" trash fa-solid fa-trash"></i>
    </div>
     <textarea></textarea>    
    `;

note.querySelector(".trash").addEventListener(
    "click", function(){
        note.remove()
    }
)
note.querySelector(".disk").addEventListener(
    "click",function(){
        saveNote()
    }
)

main.appendChild(note);

 }