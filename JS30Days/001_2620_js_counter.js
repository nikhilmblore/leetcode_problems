var createCounter = function(n) {

    let count = -1
    
    return function() {
        count += 1
        return n + count

    };
};


// Best Approach -----------------------------------  //
// The increment happens after the value is returned
var createCounter = function(n) {

    
    return function() {
        return n++

    };
};
// ------------------------------------------------- //
