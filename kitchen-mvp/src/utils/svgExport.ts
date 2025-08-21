import { saveAs } from 'file-saver';
import type { BomRow } from './bom';

export function exportPanelsSVG(rows: BomRow[]) {
  const scale = 0.5; // px per mm
  const padding = 10;
  let yOffset = padding;
  const elements: string[] = [];

  rows.forEach((r) => {
    const w = r.width * scale;
    const h = r.height * scale;
    elements.push(`<rect x="${padding}" y="${yOffset}" width="${w}" height="${h}" fill="none" stroke="black" />`);
    elements.push(`<text x="${padding + 4}" y="${yOffset + 14}" font-size="12">${r.id} ${r.width}x${r.height}</text>`);
    yOffset += h + padding;
  });

  const svg = `\n<svg xmlns="http://www.w3.org/2000/svg" width="${500}" height="${yOffset + padding}">\n${elements.join('\n')}\n</svg>`;
  const blob = new Blob([svg], { type: 'image/svg+xml;charset=utf-8' });
  saveAs(blob, 'panels.svg');
}
