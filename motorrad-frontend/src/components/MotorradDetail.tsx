import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getTuttiContent } from '../services/api';
import { Typography, Button, Container } from '@mui/material';

interface Motorrad {
  id: string;
  Titel: string;
  Link: string;
  Beschreibung: string;
  Preis: string;
  Ort: string;
  "Bild-URL": string;
}

const MotorradDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>(); 
  const [motorrad, setMotorrad] = useState<Motorrad | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      const tuttiContent = await getTuttiContent();
      const selectedMotorrad = tuttiContent.find((m: Motorrad) => m.id === id);
      setMotorrad(selectedMotorrad || null);
    };

    fetchData();
  }, [id]);

  if (!motorrad) {
    return <Typography>Lade...</Typography>;
  }

  return (
    <Container>
      <div style={{ display: 'flex', marginTop: '2rem' }}>
        <div style={{ flex: 1, marginRight: '2rem' }}>
          <img
            src={motorrad["Bild-URL"]}
            alt={motorrad.Titel}
            style={{ width: '100%', borderRadius: '8px' }}
          />
        </div>

        <div style={{ flex: 2 }}>
          <Typography variant="h4" gutterBottom>
            {motorrad.Titel}
          </Typography>
          <Typography variant="h5" color="primary" gutterBottom>
            {motorrad.Preis}
          </Typography>
          <Typography variant="body1" gutterBottom>
            <strong>Ort:</strong> {motorrad.Ort}
          </Typography>
          <Typography variant="body1" gutterBottom>
            <strong>Beschreibung:</strong> {motorrad.Beschreibung}
          </Typography>
          <Button
            variant="contained"
            color="primary"
            onClick={() => window.open(motorrad.Link, '_blank')}
          >
            Zum Inserat
          </Button>
        </div>
      </div>
    </Container>
  );
};

export default MotorradDetail;