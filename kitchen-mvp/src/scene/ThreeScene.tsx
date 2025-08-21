import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import type { ReactNode } from 'react';

interface ThreeSceneProps {
  children: ReactNode;
}

export default function ThreeScene({ children }: ThreeSceneProps) {
  return (
    <Canvas camera={{ position: [2, 2, 2], fov: 50 }}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 5, 5]} intensity={0.8} />
      <OrbitControls enablePan={false} />
      {children}
    </Canvas>
  );
}
