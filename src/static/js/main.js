function confirmDelete(event){
    const ok = confirm("Are you sure?");
    if(!ok) event.preventDefault();
}