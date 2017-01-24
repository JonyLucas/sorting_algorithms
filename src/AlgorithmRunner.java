/**
 * Interface para executar algor�tmo com lista.
 * 
 * @author Mateus Pires Lustosa
 */

public interface AlgorithmRunner {

	public <T extends Comparable<T>> long run(T[] items);
	
}
