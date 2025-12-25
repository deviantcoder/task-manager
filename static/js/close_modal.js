document.body.addEventListener("htmx:afterRequest", function (e) {
    if (e.detail.xhr.getResponseHeader("HX-Trigger")?.includes("close")) {
        const modalEl = document.getElementById("modal");
        const modal = bootstrap.Modal.getInstance(modalEl);
        if (modal) modal.hide();
    }
});
