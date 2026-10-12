# FD-322 — Three near-one Farey-index defects carry macroscopic energy without reflection

**Status:** EXACT-DERIVED + PNT-ASSISTED-ASYMPTOTIC + NEGATIVE/CONTROL-DESIGN + SHARP-THREE-POSITIVE-INDEX-BREAKS.

FD-321 established that three nonintegral Hall--Shiu stitches are minimal among nonidentity permutations of complete prime-order Farey excursions with fixed sentinels, but its first stitched index tends to zero. FD-319 retains indices approaching the admissible positive integer 1, at the cost of four defects and reflection symmetry. The positivity gap can be closed **without reflection**: three defects, all tending to 1 with total distance to the integers only 4/p, already transport a positive macroscopic amount of quadratic Farey discrepancy energy.

Let p>=7 be prime, N=N_p=sum_(q<=p) phi(q), and 0=x_0<...<x_N=1 the genuine order-p Farey grid. There is an explicit increasing rational grid x*_0=0<...<x*_N=1, made by permuting whole denominator-p excursions, which has precisely the same **directed denominator-edge multiset**, gap multiset and two outer boundary edges as F_p. Exactly three of its N-1 interior denominator indices are nonintegral. In their order along the reconstructed grid they equal

\[
\begin{array}{c|ccc}
p\bmod 6 & \nu_1 & \nu_2 & \nu_3\\ \hline
1 & 1-1/p & 1+2/p & 1-1/p\\
5 & 1-2/p & 1+1/p & 1+1/p .
\end{array} \tag{1}
\]

Every defective index tends to the *positive* integer 1; the total nearest-integer defect is exactly 4/p, with maximum 2/p. In contrast, if E_p=sum_(k=1)^(N-1)(x_k-k/N)^2 and E*_p denotes the corresponding energy of the reassembled grid, then

\[
\boxed{\lim_{\substack{p\to\infty\\p\equiv1\ (6)}}(E_p^*-E_p)=\frac1{6\pi^2},
\qquad
\lim_{\substack{p\to\infty\\p\equiv5\ (6)}}(E_p^*-E_p)=\frac1{4\pi^2}.} \tag{2}
\]

Both limits are unconditional. Fixed normalized Dirichlet sine modes also have explicit nonzero limits and exhaust the entire limiting energy; no spectral mass needs to escape to diverging frequencies. This sharpens FD-321 under its formerly missing positive-index condition, while retaining FD-319's distinct reflection-symmetric four-defect minimum.

## 1. Three cuts with nearby modular inverses

As in FD-316/FD-320, write E_j for the complete denominator-edge excursion from j/p to (j+1)/p, 1<=j<=p-2. Each excursion starts and ends at denominator p and has geometric width 1/p. Define cut labels

\[
(k,c)=
\begin{cases}
((p+1)/2,\ (2p+1)/3),&p\equiv1\pmod6,\\
((p+1)/3,\ (p+1)/2),&p\equiv5\pmod6.
\end{cases} \tag{3}
\]

For every such prime, 1<k<c<=p-2. Put A=E_1...E_(k-1), B=E_k...E_(c-1), R=E_c...E_(p-2). Replace the genuine inner order A B R by **B A R**, retaining the external 1-to-p and p-to-1 edges. Since every E_j is a closed p-to-p denominator path, this is a permutation of the genuine directed edges with their multiplicities. Assign each reordered edge (q,q') the positive gap 1/(qq') and sum the gaps from zero. The sum is still one, and all grid points are rational.

FD-320's exact stitch formula, with sentinels 0 and p-1, is

\[
\nu_{j,\ell}=1+\frac{[ (j+1)^{-1}]_p-[\ell^{-1}]_p}{p}. \tag{4}
\]

The three changed interfaces are (0,k), (c-1,1) and (k-1,c). Their modular-inverse triple is ([1^{-1}]_p,[k^{-1}]_p,[c^{-1}]_p)=(1,2,3) for p=1 (mod 6), and (1,3,2) for p=5 (mod 6). Substituting in (4) gives exactly (1). None of the three indices is integral; all other stitches retain the genuine integral index. There are no hidden boundary defects. FD-321's break-count argument proves that three is minimal for any nonidentity permutation within this *full-excursion* family; this is not a minimality assertion about arbitrary labeled paths.

## 2. Exact transport identity

Let L_A and L_B denote the gap counts of A and B, so L_A=rank(k/p)-1 and L_B=rank(c/p)-rank(k/p), where rank is the original zero-based Farey rank. Define

\[
w_A=\frac{L_A}{N}-\frac{k-1}{p},
\qquad
w_B=\frac{L_B}{N}-\frac{c-k}{p}. \tag{5}
\]

On moving B ahead of A, B's points move left by (k-1)/p geometrically and earlier by L_A ranks. Their discrepancies therefore shift by +w_A. The points of A move right by (c-k)/p and later by L_B ranks, with shift -w_B. Every remaining point keeps its discrepancy. Precisely, for a permutation P of the genuine interior discrepancy coordinates D=(x_i-i/N)_(1<=i<N),

\[
D^*=PD+v,\qquad
v_i=
\begin{cases}
w_A,&2\le i\le L_B+1,\\
-w_B,&L_B+2\le i\le L_B+L_A+1,\\
0,&\text{otherwise}.
\end{cases} \tag{6}
\]

Consequently the **finite**, exact transport energy and error formulae are

\[
T_p=\|v\|_2^2=L_Bw_A^2+L_Aw_B^2,\qquad
E_p^*-E_p=T_p+2\langle PD,v\rangle . \tag{7}
\]

Equations (5)--(7) require no asymptotic argument, probabilistic null model, or reflection assumption.

## 3. Rational-anchor ranks and the two energy limits

A small extra input is required to obtain the *first-order* rank errors at the rational cuts, not merely their limiting proportions. For fixed alpha in {1/3,2/3} write rho_p(alpha) for the number of positive Farey points <=alpha. Möbius inversion gives the exact counting relation

\[
\rho_p(\alpha)=\sum_{d\le p}\mu(d)
\sum_{m\le\lfloor p/d\rfloor}\lfloor\alpha m\rfloor,\qquad
N=\sum_{d\le p}\mu(d)
\sum_{m\le\lfloor p/d\rfloor}m. \tag{8}
\]

For either alpha, the fractional parts {alpha m} are periodic with mean 1/3, so
\(\sum_{m\le t}(\lfloor\alpha m\rfloor-\alpha m)=-t/3+h_\alpha(t)\)
with bounded, integer-periodic h_alpha(t). Since
\(\sum_{d\le p}\mu(d)\lfloor p/d\rfloor=1\),

\[
\rho_p(\alpha)-\alpha N
=-\frac13+\sum_{d\le p}\mu(d)
h_\alpha(\lfloor p/d\rfloor)=o(p). \tag{9}
\]

For clarity, the last estimate uses only the prime number theorem M(x)=o(x). Split the d-sum at epsilon*p. The smaller d contribute O(epsilon*p). On d>epsilon*p, the integer floor(p/d) takes only finitely many values (for fixed epsilon), each over an interval of d of length O(p); its Möbius sum is a difference of M at proportional arguments and hence o(p). Let p tend to infinity and then epsilon tend to zero. This proves (9) without RH.

The point (p+1)/(2p) is the immediate right Farey neighbor of 1/2, at rank N/2+1. For p=1 (mod 6), (2p+1)/(3p) is the immediate right neighbor of 2/3; for p=5 (mod 6), (p+1)/(3p) is the immediate right neighbor of 1/3. These assertions follow from determinant one and denominator sums exceeding p. Thus (9) implies:

\[
\begin{array}{c|cc|cc}
p\bmod6 &L_A/N&L_B/N&p\,w_A&p\,w_B\\ \hline
1 &1/2&1/6+o(1/p)&1/2&1/6+o(1)\\
5 &1/3+o(1/p)&1/6+o(1/p)&2/3+o(1)&-1/6+o(1).
\end{array} \tag{10}
\]

In the first row, L_A/N=1/2 and p*w_A=1/2 hold **exactly** for every p in that congruence class. The standard totient asymptotic gives N/p^2->3/pi^2. Substituting (10) into (7) therefore yields

\[
T_p\longrightarrow
\frac3{\pi^2}\left(\frac1{6}\frac1{4}+
\frac1{2}\frac1{36}\right)=\frac1{6\pi^2}
\quad(p\equiv1\!\!\pmod6)
\]

and

\[
T_p\longrightarrow
\frac3{\pi^2}\left(\frac1{6}\frac4{9}+
\frac1{3}\frac1{36}\right)=\frac1{4\pi^2}
\quad(p\equiv5\!\!\pmod6). \tag{11}
\]

FD-002 and FD-318 establish the unconditional E_p=o(1) from their exact Franel--Mertens identity, dominated convergence, and PNT. Since T_p stays bounded, the cross term in (7) is at most 2*sqrt(E_p*T_p)=o(1). Thus E_p^*-E_p=T_p+o(1), proving (2). In particular, the existence of two distinct residue-class limits does not imply an unconditional single limit along all primes.

## 4. Fixed spectral modes exhaust the energy

For fixed m>=1 let
\(d_m^*(p)=\sqrt{2/N}\sum_{i=1}^{N-1}D_i^*\sin(\pi mi/N)\).
The contribution of PD tends to zero in every mode (indeed in full spectral l^2) by FD-320 and E_p=o(1). The rescaled transport vector p*v converges, as a rank-coordinate step profile, to

\[
g_+(t)=
\begin{cases}
1/2,&0<t<1/6,\\
-1/6,&1/6<t<2/3,\\
0,&2/3<t<1,
\end{cases}
\qquad
g_-(t)=
\begin{cases}
2/3,&0<t<1/6,\\
1/6,&1/6<t<1/2,\\
0,&1/2<t<1.
\end{cases} \tag{12}
\]

The + and - signs refer to p congruent to 1 or 5 modulo 6. Riemann-sum convergence and sqrt(2N)/p->sqrt(6)/pi yield

\[
d_m^*(p)\longrightarrow \frac{\sqrt6}{\pi}
\int_0^1g_\pm(t)\sin(\pi mt)\,dt
=
\begin{cases}
\dfrac{\sqrt6}{6\pi^2m}
[3-4\cos(\pi m/6)+\cos(2\pi m/3)],&p\equiv1\pmod6,\\[5pt]
\dfrac{\sqrt6}{6\pi^2m}
[4-3\cos(\pi m/6)-\cos(\pi m/2)],&p\equiv5\pmod6.
\end{cases} \tag{13}
\]

The sine basis is complete in L^2(0,1), so the sum of squares of the limits is
\((3/\pi^2)\int_0^1g_\pm(t)^2dt\), respectively 1/(6pi^2) and 1/(4pi^2) by (11). This equals the total energy limit. Finite sine Parseval then excludes a positive residual confined to modes whose indices grow with p.

## 5. Independent falsification, prior art, and limits

Independent enumeration of the original Farey neighbors, segmentation at every denominator-p vertex, reassembly, and direct reconstruction from gaps checked primes 7, 11, 13, 17, 19, 29, 101, 103, 211 and 809. Every test preserved the directed-edge multiset and gave the three indices in (1); exact rational evaluations at p=7 and 11 yielded, respectively, E*_7-E_7=11/980 with T_7=1/49, and E*_11-E_11=30539/914760 with T_11=7/242. At p=211 (class 1), E*_p-E_p was approximately 0.01687793459 against the limit 0.01688686394; at p=809 (class 5), it was approximately 0.02440747528 against the limit 0.02533029591. The independent implementation also checked (6) pointwise up to floating-point precision and the first four fixed sine modes. These finite tests are falsification controls, **not** the proof of the asymptotics.

The Farey neighbor criterion, Hall--Shiu/BCZ index, inverse-denominator formula, totient asymptotics, Möbius inversion, PNT, and Franel--Mertens identity are classical or already derived/sourced in FD-002 and FD-315--FD-321 and this line's SOURCES.md. Boca--Gologan--Zaharescu (Quarterly Journal of Mathematics 53, 2002, 377--391, DOI 10.1093/qjmath/53.4.377) is the classical Farey-index distribution boundary. García (Mathematics 14, 2026, 2543, DOI 10.3390/math14142543) studies gap permutations for a different average local discrepancy quantity. A targeted prior-art audit found no identical **three positive-near-one stitch defects plus macroscopic Dirichlet energy** certificate in those sources; no exhaustive priority/novelty claim is implied. The new contribution claimed here is only the explicit matched labeled-edge control and its exact/conditional-on-classical-PNT energy and spectral consequences.

As in FD-319--FD-321, reconstructed denominator labels at a defective join are not the genuine reduced denominators of the new point. These are **not** alternative Farey sequences, and FD-315's exact-stitching rigidity is not contradicted. The construction does not preserve reflection, provides no improved bound for genuine Farey discrepancy or Mertens cancellation, and proves nothing toward RH beyond the precise noncoercivity of these particular weakened local-order controls. The remaining problem is which *source-natural quantitative constraints on cumulative excursion transport*, beyond the count or size of defective indices, could actually control the Franel energy.
