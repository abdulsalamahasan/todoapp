var checkbox_length = $("input[type=checkbox][name=checkbox]").length;

let checkboxes = $("input[type=checkbox][name=checkbox]")
let enabledSettings = [];

// Attach a change event handler to the checkboxes.
checkboxes.change(function() {
  enabledSettings = checkboxes
    .filter(":checked") // Filter out unchecked boxes.
    .map(function() { // Extract values using jQuery map.
      return this.value;
      var thiss = document.getElementsByClassName(this);
      console.log(thiss);
    }) 
    .get() // Get array.
    
  console.log(enabledSettings);
});