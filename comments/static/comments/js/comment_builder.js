function dateTimeSplit(isoDate) {
    let dateTimeArray = isoDate.split("T")
    let date = dateTimeArray[0]
    let time = dateTimeArray[1].slice(0, 5)
    return {"date": date, "time": time}
}

function styleValuesIncrement(currentValue, incrementByInt, valueUnit) {
    // declaring valid units
    let attributesArray = [
        "px", "pt" , "%", "em", "rem",
        "vh", "vw", "fr", "PC", "mm",
        "cm", "ex", "ch", "vmin", "vmax",    
    ]
    // validating provided unit
    if (attributesArray.includes(valueUnit)) {
        // incrementing current value with value to be plussed
        let currentValueInt = currentValue.replace(valueUnit, "");
        var finalValue = +currentValueInt + incrementByInt;
        return finalValue + valueUnit;
        
    } else {
        throw new Error(`Unit value not valid. Valide values are: ${attributesArray}`)
    }
    
};

function generateCommentContainer(data) {
    // Body
    var commentBody = document.createElement("div")
    commentBody.setAttribute("class", "comment-body")
    // Header Root
    var commentHeader = document.createElement("div")
    commentHeader.setAttribute("class", "comment-header")
    // Header-SubSection
    var headerSubSection = document.createElement("div")
    headerSubSection.setAttribute("class", "comment-header-sub")
    commentHeader.appendChild(headerSubSection)
    // Header-Rating
    var headerRating = document.createElement("div")
    headerRating.setAttribute("class", "comment-rating-container")
    commentHeader.appendChild(headerRating)

    // Content
    var commentContent = document.createElement("div")
    commentContent.setAttribute("class", "comment-content")
    var commentContentText = document.createElement("span")
    commentContentText.setAttribute("class", "comment-text")

    // appending comment child sections to body
    commentContent.appendChild(commentContentText)
    commentBody.appendChild(commentHeader)
    commentBody.appendChild(commentContent)
    
    // header
        // avatar constructing
    if (data.user.avatar) {
        var avatarPath = data.user.avatar
    } else {
        var avatarPath = defaultUserAvatar
    }

    var avatar = document.createElement("img")
    avatar.setAttribute("class", "user-avatar")
    avatar.setAttribute("src", avatarPath)
    avatar.setAttribute("alt", "UserAvatar")
        // Nickname
    var userNickname = document.createElement("span")
    userNickname.setAttribute("class", "user-username")
    userNickname.textContent = data.user.username
        // time
    var creationTime = dateTimeSplit(data.date_created);
    var creationTimeContainer = document.createElement("span");
    creationTimeContainer.setAttribute("class", "comment-time");
    creationTimeContainer.textContent = `${creationTime.date} в ${creationTime.time}`;
    
    headerSubSection.appendChild(avatar);
    headerSubSection.appendChild(userNickname);
    headerSubSection.appendChild(creationTimeContainer);

        // rating
            //UP
    var arrowUpImage = document.createElement("img");
    arrowUpImage.setAttribute("class", "rating-arrow");
    arrowUpImage.setAttribute("src", arrowUpPath);
    arrowUpImage.setAttribute("alt", "rating-up");
            // DOWN
    var arrowDownImage = document.createElement("img");
    arrowDownImage.setAttribute("class", "rating-arrow");
    arrowDownImage.setAttribute("src", arrowDownPath);
    arrowDownImage.setAttribute("alt", "rating-dow");
            // Rating score
    var ratingScore = document.createElement("span")
    ratingScore.textContent = data.rate
    if (data.rating > 0) {
        ratingScore.style.color = "green";
    } else if (data.rating < 0) {
        ratingScore.style.color = "red";
    } else {
        ratingScore.style.color = "grey";
    }

    headerRating.appendChild(arrowUpImage)
    headerRating.appendChild(ratingScore)
    headerRating.appendChild(arrowDownImage)

    // content
    commentContentText.textContent = data.text

    // adding left marging if child

   return commentBody 
}


function commentTreeBuilder(comment, parentContainer, parent=null) {
        
        let commentDiv = generateCommentContainer(comment); 
        if (parent) {  
            let parentMargin = parent.style.marginLeft
            commentDiv.style.marginLeft = styleValuesIncrement(parentMargin, 15, "px")
        }
        // constructing HTML <div> body
         

        let childrenArraySize = Object.keys(comment.children).length;

        if (childrenArraySize !== null && childrenArraySize > 0) { 
            // creation of wrapper for comment tree
            let parentCommentWrapper = document.createElement("div");
            parentCommentWrapper.setAttribute("class", "comment-wrapper");
            parentCommentWrapper.appendChild(commentDiv)
            parentContainer.appendChild(parentCommentWrapper)

            // iterationg over child comments array 
            for (const child of comment.children) {

                commentTreeBuilder(child, parentCommentWrapper, commentDiv);   
            };  
        } else {
            parentContainer.appendChild(commentDiv)
        }
}
