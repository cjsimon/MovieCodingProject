import * as ejs from "./ejs/ejs.min.js";

export default class {
    // Expose the helper ejs library from this driver class
    ejs = ejs;
    
    /** Only render "text/javascript-template" script tags as ejs templates */
    static render(templateData) {
        return function() {
            var templates = document.querySelectorAll('script[type="text/javascript-template"]');
            
            templates.forEach(function(template) {
                // Compile the unrendered template, passing in the template data to use
                var renderedTemplate = ejs.compile(template.innerHTML, { client: true })(templateData);
                
                // Inject the rendered template back into the DOM,
                // in-place of the unrendered template
                template.outerHTML = renderedTemplate;
            });
        }
    };
    
    /** Render the whole page body as an ejs template */
    static renderPage(templateData) {
        return function() {
            document.body.innerHTML = ejs.compile(document.body.innerHTML, { client: true })(templateData);
        };
    };
};
