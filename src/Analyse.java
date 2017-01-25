/**
 * Classe que armazena os dados resultantes da an�lise.
 * 
 * @author Mateus Pires Lustosa
 */
public class Analyse {

	public final long time;
	public final int runs;
	
	public Analyse(long time, int runs)
	{
		this.time = time;
		this.runs = runs;
	}
	
	/* Retorna a m�dia de tempo. */
	public double getTime() { return time / (double) runs; }
	
}
