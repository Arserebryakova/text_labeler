function debounce(func, wait, immediate) {
    var timeout;
    return function () {
        var context = this, args = arguments;
        var later = function () {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        var callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
};


document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.getElementById("text_input_form");
    const labelSelector = document.getElementById("label_selector");

    var callLabelText = function () {
        const inputText = textarea.value; // Get the current value of the textarea
        const labelType = labelSelector.value;
        console.log(labelType)

        // Send POST request to /api/method
        fetch("/api/label_text", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                text: inputText,
                label_type: labelType
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                const labeledText = data.labeled_text;
                console.log("Received text:", labeledText);
                output_text = '<span class="py-2">Labeled text</span>' + labeledText
                document.getElementById("labeled_text").innerHTML = output_text;
            })
            .catch((error) => console.error("Error:", error));
    }

    var msTimeoutBetweenCalls = 500;
    textarea.addEventListener("input", debounce(callLabelText, msTimeoutBetweenCalls));
    labelSelector.addEventListener("change", debounce(callLabelText, msTimeoutBetweenCalls));
    callLabelText() // first call to label sample data
});
