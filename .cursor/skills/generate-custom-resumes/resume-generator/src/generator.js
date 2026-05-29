import Handlebars from 'handlebars';
import puppeteer from 'puppeteer';
import fs from 'fs-extra';
import path from 'path';
import { fileURLToPath } from 'url';
import { loadYAML, mergeResumes } from './parser.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Register Handlebars helper to convert simple markdown to HTML
// Supports: **bold**, `code`, and → arrow
Handlebars.registerHelper('md', function(str) {
  if (!str) return '';
  if (typeof str !== 'string') return str;
  const html = str
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/`(.+?)`/g, '<code>$1</code>');
  return new Handlebars.SafeString(html);
});

// Register Handlebars helper for splitting strings by paragraphs
// Handles both | (literal) and > (folded) YAML block scalars
Handlebars.registerHelper('splitLines', function(str) {
  if (!str) return [];
  // Split by double newlines (paragraph breaks) or single newlines if no double newlines exist
  // This handles both | (literal) and > (folded) YAML block scalars
  const paragraphs = str.split(/\n\s*\n/).filter(p => p.trim());
  // If no paragraph breaks found, split by single newlines (backward compatibility)
  if (paragraphs.length === 1 && str.includes('\n')) {
    return str.split('\n').filter(line => line.trim());
  }
  return paragraphs.map(p => p.replace(/\n/g, ' ').trim());
});

/**
 * Load template and CSS files
 */
function loadTemplate() {
  const templatePath = path.join(__dirname, 'templates', 'resume.hbs');
  const cssPath = path.join(__dirname, 'templates', 'styles.css');
  
  const templateContent = fs.readFileSync(templatePath, 'utf8');
  const cssContent = fs.readFileSync(cssPath, 'utf8');
  
  return {
    template: Handlebars.compile(templateContent),
    css: cssContent
  };
}

/**
 * Generate PDF from resume data
 * @param {Object} resumeData - Merged resume data
 * @param {string} outputPath - Path to save the PDF
 */
export async function generatePDF(resumeData, outputPath) {
  const { template, css } = loadTemplate();
  
  // Prepare data for template
  const templateData = {
    ...resumeData,
    css: css
  };
  
  // Render HTML
  const html = template(templateData);

  // Generate PDF using Puppeteer
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  try {
    const page = await browser.newPage();
    
    // Set content
    await page.setContent(html, {
      waitUntil: 'networkidle0'
    });
    
    // Generate PDF
    await page.pdf({
      path: outputPath,
      format: 'A4',
      printBackground: true,
    });
    
    console.log(`✅ PDF generated: ${outputPath}`);
  } finally {
    await browser.close();
  }
}

/**
 * Generate resume from base and optional customization
 * @param {string} basePath - Path to base resume YAML
 * @param {string} customPath - Optional path to customization YAML
 * @param {string} outputPath - Path to save the PDF
 */
export async function generateResume(basePath, customPath = null, outputPath) {
  try {
    // Load base resume
    const baseResume = loadYAML(basePath);
    
    // Load customization if provided
    let customResume = null;
    if (customPath && fs.existsSync(customPath)) {
      customResume = loadYAML(customPath);
    }
    
    // Merge resumes
    const mergedResume = mergeResumes(baseResume, customResume);
    
    // Ensure output directory exists
    const outputDir = path.dirname(outputPath);
    await fs.ensureDir(outputDir);
    
    // Generate PDF
    await generatePDF(mergedResume, outputPath);
    
    return mergedResume;
  } catch (error) {
    console.error('❌ Error generating resume:', error.message);
    throw error;
  }
}

/**
 * Generate cover letter PDF from a markdown file and base resume header info
 * @param {Object} resumeData - Resume data (for header: name, email, links)
 * @param {string} outputPath - Path to save the PDF
 * @param {string} coverLetterContent - Raw markdown text of the cover letter
 */
export async function generateCoverLetterPDF(resumeData, coverLetterContent, outputPath) {
  const templatePath = path.join(__dirname, 'templates', 'cover-letter.hbs');
  const cssPath = path.join(__dirname, 'templates', 'styles.css');

  const templateContent = fs.readFileSync(templatePath, 'utf8');
  const cssContent = fs.readFileSync(cssPath, 'utf8');
  const template = Handlebars.compile(templateContent);

  // Split cover letter into paragraphs (blank-line separated)
  const paragraphs = coverLetterContent
    .split(/\n\s*\n/)
    .map(p => p.replace(/\n/g, ' ').trim())
    .filter(p => p.length > 0);

  const templateData = {
    name: resumeData.name,
    email: resumeData.email,
    links: resumeData.links,
    paragraphs,
    css: cssContent,
  };

  const html = template(templateData);

  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  try {
    const page = await browser.newPage();
    await page.setContent(html, { waitUntil: 'networkidle0' });
    await page.pdf({
      path: outputPath,
      format: 'A4',
      printBackground: true,
    });
    console.log(`✅ Cover letter PDF generated: ${outputPath}`);
  } finally {
    await browser.close();
  }
}

/**
 * Generate cover letter from a markdown file and base resume
 * @param {string} basePath - Path to base resume YAML (for header info)
 * @param {string} customPath - Optional path to customization YAML
 * @param {string} coverLetterPath - Path to the cover letter markdown file
 * @param {string} outputPath - Path to save the cover letter PDF
 */
export async function generateCoverLetter(basePath, customPath = null, coverLetterPath, outputPath) {
  try {
    const baseResume = loadYAML(basePath);

    let customResume = null;
    if (customPath && fs.existsSync(customPath)) {
      customResume = loadYAML(customPath);
    }

    const mergedResume = mergeResumes(baseResume, customResume);

    if (!fs.existsSync(coverLetterPath)) {
      throw new Error(`Cover letter file not found: ${coverLetterPath}`);
    }

    const coverLetterContent = fs.readFileSync(coverLetterPath, 'utf8');

    const outputDir = path.dirname(outputPath);
    await fs.ensureDir(outputDir);

    await generateCoverLetterPDF(mergedResume, coverLetterContent, outputPath);
  } catch (error) {
    console.error('❌ Error generating cover letter:', error.message);
    throw error;
  }
}
