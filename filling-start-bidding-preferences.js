/* 

Steps:
------
1) Make selections for papers you want to review
2) Order the papers by the bids
3) Find the "index" of the first row with missing preferences (zero-indexed)
4) Set the value of the "first_index_to_ignore" variable to this "index"

*/

var first_index_to_ignore = 24;
var rows = document.getElementById("t1").rows;

for (var i=first_index_to_ignore; i< rows.length; i++)
{
    // Get the paper's id
    var id = rows[i].getElementsByTagName("td")[0].innerHTML.replace(/\s/g, '');
    // Call the js function to set the preference for this paper to "No"
    updateBids(id, 3);
}
