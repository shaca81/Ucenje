import { saveAs } from 'file-saver';
import type { CabinetParams } from '../components/ParametricCabinet';

export interface BomRow {
  id: string;
  part: string;
  width: number; // mm
  height: number; // mm
  thickness: number; // mm
  material: string;
}

export function generateCabinetBOM({ width, height, depth, thickness = 18 }: CabinetParams): BomRow[] {
  const t = thickness;
  const innerW = width - 2 * t;
  const innerH = height - t;

  return [
    { id: 'left', part: 'side', width: depth, height, thickness: t, material: 'default' },
    { id: 'right', part: 'side', width: depth, height, thickness: t, material: 'default' },
    { id: 'bottom', part: 'bottom', width: innerW, height: depth, thickness: t, material: 'default' },
    { id: 'back', part: 'back', width: innerW, height: innerH, thickness: t, material: 'default' },
    { id: 'door', part: 'door', width, height, thickness: t, material: 'default' },
  ];
}

export function exportBOMCSV(rows: BomRow[]) {
  const header = 'id,part,width_mm,height_mm,thickness_mm,material';
  const lines = rows.map(r => `${r.id},${r.part},${r.width},${r.height},${r.thickness},${r.material}`);
  const csv = [header, ...lines].join('\n');
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  saveAs(blob, 'bom.csv');
}
