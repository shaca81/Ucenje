import { useState } from 'react';
import ThreeScene from './scene/ThreeScene';
import ParametricCabinet from './components/ParametricCabinet';
import type { CabinetParams } from './components/ParametricCabinet';
import { generateCabinetBOM, exportBOMCSV } from './utils/bom';
import { exportPanelsSVG } from './utils/svgExport';
import './App.css';

function App() {
  const [params, setParams] = useState<CabinetParams>({ width: 600, height: 720, depth: 560 });

  const handleChange = (key: keyof CabinetParams, value: number) => {
    setParams({ ...params, [key]: value });
  };

  const bom = generateCabinetBOM(params);

  return (
    <div className="app-container">
      <div className="controls">
        <h2>Cabinet Parameters (mm)</h2>
        <label>
          Width
          <input type="number" value={params.width} onChange={(e) => handleChange('width', Number(e.target.value))} />
        </label>
        <label>
          Height
          <input type="number" value={params.height} onChange={(e) => handleChange('height', Number(e.target.value))} />
        </label>
        <label>
          Depth
          <input type="number" value={params.depth} onChange={(e) => handleChange('depth', Number(e.target.value))} />
        </label>
        <button onClick={() => exportBOMCSV(bom)}>Export BOM CSV</button>
        <button onClick={() => exportPanelsSVG(bom)}>Export Panels SVG</button>
      </div>
      <div className="viewer">
        <ThreeScene>
          <ParametricCabinet {...params} />
        </ThreeScene>
      </div>
    </div>
  );
}

export default App;
