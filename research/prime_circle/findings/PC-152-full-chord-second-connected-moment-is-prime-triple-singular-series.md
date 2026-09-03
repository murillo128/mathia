# PC-152 — full-chord second connected moment is a prime-triple singular-series functional

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY`. PC-149 proves that every fixed local chord word is an exact generalized-totient / Hardy--Littlewood tuple count, PC-150 upgrades fixed-radius scalar spectral functions to a pair-singular-series law at first Mertens order, and PC-151 passes that first-order law to the complete all-chord inverse-square operator. The first subleading operator question left explicitly open by PC-151 is therefore whether a genuine **three-vertex interaction** appears at the next `1/log^2 x` scale rather than merely another pair correction.

For the second spectral moment this can be separated exactly, without choosing a cutoff or subtracting an asymptotic expansion. The square trace of the full primitive-shell Laplacian splits into a same-edge term and a wedge term. The same-edge term is exactly the pair law already classified by PC-151. The wedge term counts translated three-point primitive constellations and, after the natural `log^2 x / phi(N_x)` scaling, converges absolutely over **all chord lengths** to an inverse-square weighted Hardy--Littlewood prime-triple singular-series functional.

Thus the first genuinely multi-edge correction in a full-chord polynomial spectral observable does retain nonlocal three-point geometry, but its arithmetic coefficients are exactly the classical prime-triple local densities. No new zeta-zero divisor, functional equation, or critical-line symmetry is generated at this level.

## 1. The second moment separates exactly by vertex support

Let

\[
N_x:=\prod_{p\le x}p,
\qquad
\phi_x:=\varphi(N_x),
\qquad
U_x:=(\mathbb Z/N_x\mathbb Z)^\times,
\]

and let

\[
A_x:=N_x^{-2}L_{N_x}^{\rm int}
\]

be the normalized full primitive-shell inverse-square chord Laplacian of PC-151. For an unordered primitive edge `e={a,b}`, write

\[
g_e=
\frac{1}{4N_x^2\sin^2(\pi(a-b)/N_x)}
\]

with the cyclic distance understood, and choose either incidence vector

\[
b_e=e_a-e_b.
\]

Then

\[
\boxed{
A_x=\sum_e g_e\,b_e b_e^*.
}
\tag{1}
\]

The orientation of `b_e` is irrelevant. Expanding the square or, equivalently, using the usual weighted-Laplacian identity gives

\[
\boxed{
\operatorname{Tr}(A_x^2)
=4\sum_e g_e^2
+2\sum_{v\in U_x}
\sum_{\{e,f\}\subset E(v),\ e\ne f}
g_e g_f.
}
\tag{2}
\]

The first term consists of repeated traversal of one edge and therefore has support on exactly two primitive vertices. The second term consists of unordered pairs of distinct edges meeting at one primitive vertex and therefore has support on exactly three distinct vertices.

Define the **three-vertex connected correction**

\[
\boxed{
W_x:=
\operatorname{Tr}(A_x^2)-4\sum_e g_e^2.
}
\tag{3}
\]

This is an exact support decomposition, not an asymptotic subtraction. In particular it avoids any need for a second term in Mertens' product theorem.

The two-vertex part is already PC-151 with `f(t)=t^2`: if a positive chord offset is `h`, one isolated edge has nonzero eigenvalue `2g_{N_x,h}`, so the first `1/log x` contribution is precisely the prime-pair singular-series moment classified there. The new question is entirely `W_x`.

## 2. Every wedge is an exact reduced-residue triple count

For `x>=3`, put

\[
D_x:=\{h\in\mathbb Z:-N_x/2<h<N_x/2,\ h\ne0\}.
\]

The antipodal offset `N_x/2` cannot join two primitive residues: `N_x/2` is odd whereas every unit modulo the even primorial `N_x` is odd. Thus `D_x` contains every possible primitive-to-primitive neighbor displacement exactly once as a signed displacement from its center.

For `h,k\in D_x` with `h\ne k`, define

\[
J_{h,k}(N_x)
:=
\#\{a\bmod N_x:
a,a+h,a+k\in U_x\}.
\tag{4}
\]

Also write

\[
g_{N,h}:=
\frac{1}{4N^2\sin^2(\pi h/N)},
\qquad 0<|h|<N/2.
\tag{5}
\]

At a fixed center `a`, ordering the two distinct signed neighbor offsets counts every unordered wedge twice, exactly cancelling the factor `2` in (2). Hence

\[
\boxed{
W_x
=
\sum_{\substack{h,k\in D_x\\h\ne k}}
J_{h,k}(N_x)\,
 g_{N_x,h}g_{N_x,k}.
}
\tag{6}
\]

For each prime `p`, let

\[
\nu_p(h,k):=
\#\{0,h,k\pmod p\}.
\tag{7}
\]

CRT gives the exact finite product

\[
\boxed{
\frac{J_{h,k}(N_x)}{\phi_x}
=
\prod_{p\le x}
\frac{p-\nu_p(h,k)}{p-1}.
}
\tag{8}
\]

If the three offsets cover every residue modulo some prime, the product is exactly zero. Otherwise define the ordinary Hardy--Littlewood singular series of the rooted triple

\[
\boxed{
\mathfrak S_3(h,k)
:=
\prod_p
\frac{1-\nu_p(h,k)/p}{(1-1/p)^3}.
}
\tag{9}
\]

Writing

\[
M(x):=\prod_{p\le x}\left(1-\frac1p\right),
\]

equation (8) is exactly

\[
\frac{J_{h,k}(N_x)}{\phi_x}
=M(x)^2
\prod_{p\le x}
\frac{1-\nu_p(h,k)/p}{(1-1/p)^3}.
\tag{10}
\]

For every fixed admissible pair `(h,k)`, the partial singular series converges and Mertens' theorem therefore yields

\[
\boxed{
(\log x)^2
\frac{J_{h,k}(N_x)}{\phi_x}
\longrightarrow
 e^{-2\gamma}\mathfrak S_3(h,k).
}
\tag{11}
\]

The parity obstruction is already built into this formula: once `2|N_x`, a nonzero triple requires both `h` and `k` even. The modulus-3 obstruction similarly kills triples whose three offsets occupy all three classes.

## 3. The all-chord three-vertex correction has an absolutely convergent limit

The passage from fixed offsets to the complete all-chord sum is justified by the same geometric decay that made PC-151's pair tail summable, now in two variables. For `0<|h|<N/2`,

\[
\boxed{
g_{N,h}\le\frac1{16h^2}}
\tag{12}
\]

by `sin t >= 2t/pi` on `[0,pi/2]`, while for fixed `h`

\[
\boxed{
g_{N_x,h}\longrightarrow\frac1{4\pi^2h^2}.}
\tag{13}
\]

It remains to control the triple singular series uniformly. Put

\[
\Delta(h,k):=hk(h-k).
\]

For every prime `p>=5` not dividing `Delta`, the three residues are distinct and the local factor in (9) is

\[
\frac{1-3/p}{(1-1/p)^3}=1+O(p^{-2}).
\]

Only primes dividing `Delta` can increase that generic factor. At such primes the enhancement is `1+O(1/p)`; the primes `2` and `3` are a fixed finite exception. Consequently, for some absolute constant `C`,

\[
\boxed{
\mathfrak S_3(h,k)
\ll
\prod_{\substack{p\mid\Delta(h,k)\\p\ge5}}
\left(1+\frac{C}{p}\right)
\ll
\bigl(\log\log(3|\Delta(h,k)|)\bigr)^C.
}
\tag{14}
\]

The same bound holds uniformly for the partial product in (10), up to an absolute constant. Since `(log x)M(x)` is bounded, equations (10), (12), and (14) give a summable majorant of the form

\[
\frac{\operatorname{polyloglog}(|hk(h-k)|)}{h^2k^2}.
\]

The double series is absolutely convergent. Dominated convergence in (6) therefore gives the exact full-radius limit

\[
\boxed{
\lim_{x\to\infty}
\frac{(\log x)^2}{\phi_x}W_x
=
\frac{e^{-2\gamma}}{16\pi^4}
\sum_{\substack{h,k\in\mathbb Z\setminus\{0\}\\h\ne k}}
\frac{\mathfrak S_3(h,k)}{h^2k^2}.
}
\tag{15}
\]

The right side is positive and finite. It is intrinsically two-dimensional in offset space: unlike the pair law of PC-151, the coefficient depends on the collision arithmetic of all three differences `h`, `k`, and `h-k`.

Thus long chords do **not** generate an additional nonlocal arithmetic species in the second connected moment. They complete a convergent geometric weighting of the classical prime-triple singular series.

## 4. Prior-art and novelty audit

The arithmetic coefficients in (8)--(11) are classical. PC-149 already identifies simultaneous coprimality of arbitrary finite translates with the generalized Euler/Lucas-totient framework of Nittiya Pabhapote and Vichian Laohakosol, **Combinatorial Aspects of the Generalized Euler's Totient**, *International Journal of Mathematics and Mathematical Sciences* 2010, Article 648165, DOI `10.1155/2010/648165`. Equation (9) is exactly the standard Hardy--Littlewood `k`-tuple singular series specialized to `k=3`.

The averaging theory is likewise established prior art. P. X. Gallagher, **On the distribution of primes in short intervals**, *Mathematika* 23:1 (1976), 4--9, DOI `10.1112/S0025579300016442`, uses averages of fixed-size Hardy--Littlewood singular series to derive the conditional Poisson law for primes in logarithmic intervals. Vivian Kuperberg, **Sums of singular series along arithmetic progressions and with smooth weights**, *International Journal of Number Theory* 21:1 (2025), 53--74, DOI `10.1142/S1793042125500046`, studies constrained and smoothly weighted singular-series sums and shows that such weighted averages remain governed by classical incidence/pairing structure. These sources do not appear to state the exact Prime-Circle inverse-square double sum (15), and no novelty is claimed for that specialization.

The operator identity (2) is standard weighted-graph Laplacian algebra. The durable Prime-Circle content is the exact **support-stratified identification**: after the pair layer of PC-151 is removed algebraically, the first genuinely multi-edge spectral term of the complete geometric operator is already nothing more than a convergent prime-triple singular-series functional.

This is a classicalization boundary, not an RH mechanism. Equation (15) contains no free complex spectral parameter, analytic continuation, gamma factor, `s <-> 1-s` involution, or self-adjoint spectral condition for zeta zeros. One could introduce Mellin/Dirichlet variables into the two offset weights afterward, but zero dependence from such a post hoc transform would need a fresh prior-art audit; it is not generated by the second connected moment itself.

## 5. Boundary and falsification surface

1. For every finite primorial, direct matrix construction must satisfy the exact decomposition (2) and the signed-offset identity (6). One mismatch falsifies the support separation.
2. Direct CRT enumeration of any fixed `(h,k)` must satisfy (8). In particular both offsets must be even after the prime `2` enters, and a triple occupying all residues modulo `3` must vanish exactly.
3. For fixed admissible `(h,k)`, the scaled count in (11) must approach `e^{-2 gamma} mathfrak S_3(h,k)`.
4. The full double sum in (15) must be absolutely convergent; the only possible local enhancements occur at prime divisors of `hk(h-k)`, while the inverse-square chord geometry supplies the summable `h^{-2}k^{-2}` envelope.
5. This finding classifies only the **three-vertex support stratum of the second polynomial moment**. It does not prove that every `1/log^2 x` correction to an arbitrary non-polynomial spectral function is triple-classical, nor does it classify higher connected moments, eigenvectors/projectors, cross-level coherent transport, or the accepted clue's remaining non-Cauchy/infinite-depth coupling boundary.
6. A materially new continuation must therefore retain information absent from the scalar weighted triple density in (15). Merely recovering a Hardy--Littlewood triple singular series, or applying an external transform to it, does not cross the Prime-Circle novelty gate.