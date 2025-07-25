// MathJax configuration for Van Cooldown Documentation
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// Additional math configurations
document$.subscribe(() => { 
  MathJax.startup.output.clearCache?.()
  MathJax.typesetClear()
  MathJax.texReset()
  MathJax.typesetPromise()
});
