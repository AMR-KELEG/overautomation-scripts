/* 

Steps:
------
1) Make selections for papers you want to review
2) Order the papers by the bids column such that papers with preselected preferences are on top
3) Find the "index" of the first row with missing preferences (Start counting from 1)
4) Set the value of the "first_index_to_ignore" variable to this "index"
*/

// Don't forget to change this!
var first_index_to_ignore = ;

// Skip the first two rows in the table
first_index_to_ignore += 2;

var rows = document.getElementById("t1").rows;

// Loop through all the rows starting from this index and set the preference to "No"
for (var i=first_index_to_ignore; i< rows.length; i++)
{
    // Get the paper's id
    var id = rows[i].getElementsByTagName("td")[0].innerHTML.replace(/\s/g, '');
    // Call the js function to set the preference for this paper to "No"
    updateBids(id, 3);
}
