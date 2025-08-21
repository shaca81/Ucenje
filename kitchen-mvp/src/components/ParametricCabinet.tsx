import { useMemo } from 'react';
import type { ThreeElements } from '@react-three/fiber';

export interface CabinetParams {
  width: number; // in mm
  height: number; // in mm
  depth: number; // in mm
  thickness?: number; // panel thickness mm
}

const MM_TO_M = 0.001;
const DEFAULT_THICKNESS = 18;

interface PanelSpec {
  w: number; // width mm
  h: number; // height mm
  d: number; // depth mm
  position: [number, number, number]; // meters
}

function Panel({ spec }: { spec: PanelSpec }) {
  const args = [spec.w * MM_TO_M, spec.h * MM_TO_M, spec.d * MM_TO_M] as [number, number, number];
  return (
    <mesh position={spec.position}>
      <boxGeometry args={args} />
      <meshStandardMaterial color="#cccccc" />
    </mesh>
  );
}

export default function ParametricCabinet({
  width,
  height,
  depth,
  thickness = DEFAULT_THICKNESS,
  ...groupProps
}: CabinetParams & ThreeElements['group']) {
  const panels = useMemo(() => {
    const t = thickness;
    const w = width;
    const h = height;
    const d = depth;
    const innerW = w - 2 * t;
    const innerH = h - t;

    const left: PanelSpec = {
      w: t,
      h,
      d,
      position: [-(innerW / 2) * MM_TO_M, h / 2 * MM_TO_M, 0],
    };
    const right: PanelSpec = {
      w: t,
      h,
      d,
      position: [(innerW / 2) * MM_TO_M, h / 2 * MM_TO_M, 0],
    };
    const bottom: PanelSpec = {
      w: innerW,
      h: t,
      d,
      position: [0, (t / 2) * MM_TO_M, 0],
    };
    const back: PanelSpec = {
      w: innerW,
      h: innerH,
      d: t,
      position: [0, (innerH / 2 + t) * MM_TO_M, -(d / 2 - t / 2) * MM_TO_M],
    };
    const door: PanelSpec = {
      w,
      h,
      d: t,
      position: [0, (h / 2) * MM_TO_M, (d / 2 + t / 2) * MM_TO_M],
    };

    return { left, right, bottom, back, door };
  }, [width, height, depth, thickness]);

  return (
    <group {...groupProps}>
      <Panel spec={panels.left} />
      <Panel spec={panels.right} />
      <Panel spec={panels.bottom} />
      <Panel spec={panels.back} />
      <Panel spec={panels.door} />
    </group>
  );
}
