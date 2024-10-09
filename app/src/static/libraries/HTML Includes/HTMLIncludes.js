export default class {
    static fetch() {
        let includes = document.getElementsByTagName('include');
        
        [...includes].forEach(async function(element) {
            let filePath = element.getAttribute('src');
            
            let response = await fetch(filePath);
            let content  = await response.text();
            
            element.insertAdjacentHTML('afterend', content);
            element.remove();
        });
    }
};
