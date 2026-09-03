# VIS-005 — local CRT leakage obstructs uniform gap-two eigenspace locking

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

## Claim

Let

\[
N_x=\prod_{p\le x}p,\qquad x\ge 5,
\]

and let \(L_x=L_{N_x}^{\rm int}\) be the primitive-shell inverse-square chord Laplacian of `PC-142`. Write

\[
w_d(N)=\frac{1}{4\sin^2(\pi d/N)},\qquad
\beta_N=2w_2(N)=\frac{1}{2\sin^2(2\pi/N)}.
\]

Let \(V_x\) be the exact gap-two matching space, let \(Q_x=P_{V_x}\), and let \(P_x\) be the spectral projector onto the top

\[
E_x=\prod_{3\le p\le x}(p-2)
\]

eigenvalues of \(L_x\). By `PC-142`, this band is unambiguously isolated: it consists of exactly \(E_x\) eigenvalues at or above \(\beta_{N_x}\), separated from the rest by a positive \(N_x^2\)-scale gap.

The finite visualization `primitive-shell-gap2-spectral-locking` suggested that \(P_x\) is extremely close to \(Q_x\). The exact local geometry gives a stricter conclusion in the **worst principal angle**: the two projectors cannot converge in operator norm. If \(N_x=6m_x\), define

\[
g_x=
\frac{w_4(N_x)-w_6(N_x)}{\sqrt2},
\qquad
D_x=\frac{5m_x^2-1}{6}.
\]

Then

\[
\boxed{
\|P_x-Q_x\|
\ge
\frac{g_x}{2D_x}
}
\tag{1}
\]

and therefore

\[
\boxed{
\liminf_{x\to\infty}\|P_x-Q_x\|
\ge
\frac{3}{16\sqrt2\,\pi^2}
=
0.0134334\ldots>0.
}
\tag{2}
\]

Since equal-rank orthogonal projectors satisfy
\(\|P_x-Q_x\|=\sin\theta_{\max}(P_x,Q_x)\), asymptotic locking in the strongest principal-angle sense is impossible.

There is a different conclusion for **average/Frobenius locking**. Put

\[
C_x=\frac{1}{E_x}\operatorname{tr}(P_xQ_x)
\]

for the normalized captured fraction used in the visualization, and let

\[
M_x=\prod_{7\le p\le x}(p-3).
\]

Then

\[
\boxed{
1-C_x
\ge
\frac{M_x}{E_x}\,
\frac{g_x^2}{4D_x^2}.
}
\tag{3}
\]

Moreover

\[
\frac{M_x}{E_x}
=
\frac13
\prod_{7\le p\le x}
\left(1-\frac{1}{p-2}\right)
=
\Theta\!\left(\frac1{\log x}\right),
\tag{4}
\]

while

\[
\frac{g_x^2}{4D_x^2}
\longrightarrow
\frac{9}{512\pi^4}.
\tag{5}
\]

Hence

\[
\boxed{
1-C_x=\Omega\!\left(\frac1{\log x}\right).
}
\tag{6}
\]

Equation (6) does **not** rule out \(C_x\to1\). It says that if the average/Frobenius locking converges to one, it cannot do so faster than logarithmically in the largest prime \(x\) on the strength of this exact local witness family. Thus the visual question bifurcates: worst-angle locking is now ruled out, while average locking remains a genuine asymptotic problem.

## 1. A CRT family forces an unpaired outer primitive vertex

Take an oriented primitive gap-two pair \(\{a,a+2\}\) satisfying the congruences

\[
a\equiv1\pmod2,\qquad
a\equiv2\pmod3,\qquad
a\equiv1\pmod5,
\tag{7}
\]

and, for every prime \(p\mid N_x\) with \(p\ge7\),

\[
a\not\equiv 0,-2,4\pmod p.
\tag{8}
\]

These conditions ensure that \(a\), \(a+2\), and \(a-4\) are all units modulo \(N_x\). They also force

\[
a-2\equiv0\pmod3,
\qquad
a-6\equiv0\pmod5.
\tag{9}
\]

Consequently \(c=a-4\) is a primitive vertex whose two gap-two neighbors \(c+2=a-2\) and \(c-2=a-6\) are both non-primitive. It belongs to no edge of the exact gap-two matching, so

\[
e_c\in V_x^\perp.
\tag{10}
\]

The Chinese remainder theorem counts the oriented pairs satisfying (7)--(8) exactly:

\[
\boxed{
M_x=\prod_{7\le p\le x}(p-3).
}
\tag{11}
\]

There is no double counting from the opposite orientation: the other endpoint \(a+2\) is \(1\bmod3\), whereas (7) fixes the oriented start to \(2\bmod3\).

This is the arithmetic feature missed by a pure rank/count argument. `PC-142` proves that the gap-two matching has exactly the correct **dimension** for the isolated high band. The CRT construction above shows that a positive family of those matching vectors nevertheless leaks immediately into coordinates outside the matching support.

## 2. Each witness has an exact short-chord leakage coefficient

For a witness pair define the normalized matching vector

\[
q_a=\frac{e_a-e_{a+2}}{\sqrt2}\in V_x.
\tag{12}
\]

The primitive-shell Laplacian has off-diagonal entries \(-w_{|r-s|}(N_x)\). With \(c=a-4\), the two distances from \(c\) to the endpoints of the pair are \(4\) and \(6\). Therefore

\[
\begin{aligned}
\langle e_c,L_xq_a\rangle
&=
\frac{-w_4(N_x)-(-w_6(N_x))}{\sqrt2}\\
&=
-\frac{w_4(N_x)-w_6(N_x)}{\sqrt2}\\
&=-g_x.
\end{aligned}
\tag{13}
\]

For \(N_x\ge30\), the relevant angles lie in the increasing branch of sine and \(w_4>w_6\), hence \(g_x>0\).

Let

\[
B_x=(I-Q_x)L_xQ_x.
\tag{14}
\]

Because \(e_c\in V_x^\perp\), equation (13) gives

\[
\|B_xq_a\|\ge g_x.
\tag{15}
\]

The \(M_x\) witness matching vectors are distinct members of the orthonormal gap-two matching basis. Thus

\[
\boxed{
\|B_x\|\ge g_x,
\qquad
\|B_x\|_F^2\ge M_xg_x^2.
}
\tag{16}
\]

This is an exact residual statement independent of any eigensolver, rendering, or eigenvector basis choice.

## 3. The residual becomes a projector-distance obstruction

The spectral projector \(P_x\) commutes with \(L_x\):

\[
[L_x,P_x]=0.
\tag{17}
\]

Relative to the decomposition \(V_x\oplus V_x^\perp\), the commutator with \(Q_x\) has the block form

\[
[L_x,Q_x]
=
\begin{pmatrix}
0 & -B_x^\ast\\
B_x & 0
\end{pmatrix}.
\tag{18}
\]

Hence

\[
\|[L_x,Q_x]\|=\|B_x\|,
\qquad
\|[L_x,Q_x]\|_F=\sqrt2\,\|B_x\|_F.
\tag{19}
\]

Using (17),

\[
[L_x,Q_x]=[L_x,Q_x-P_x].
\tag{20}
\]

For any matrix \(X\),

\[
\|[L_x,X]\|\le2\|L_x\|\,\|X\|,
\qquad
\|[L_x,X]\|_F\le2\|L_x\|\,\|X\|_F.
\tag{21}
\]

`PC-142` decomposes \(L_x=\beta_{N_x}Q_x+R_x\) and proves

\[
\|R_x\|
\le
\rho_{N_x}
=
\frac{5m_x^2-1}{6}-\beta_{N_x},
\qquad N_x=6m_x.
\]

Therefore

\[
\boxed{
\|L_x\|
\le
\beta_{N_x}+\rho_{N_x}
=
D_x
=
\frac{5m_x^2-1}{6}.
}
\tag{22}
\]

Combining (16), (19)--(22) yields (1):

\[
g_x
\le
\|[L_x,Q_x]\|
\le
2D_x\|Q_x-P_x\|.
\tag{23}
\]

The obstruction is therefore not a generic statement that a perturbation can rotate a subspace. It is a concrete arithmetic lower bound: the exact local CRT witness makes \(V_x\) non-invariant by a fixed \(N_x^2\)-scale fraction, and a truly convergent spectral projector would force that commutator to vanish in the same normalized scale.

## 4. The worst-angle lower bound has a positive asymptotic limit

As \(m_x\to\infty\),

\[
w_4(N_x)
=
\frac{9m_x^2}{16\pi^2}+O(1),
\qquad
w_6(N_x)
=
\frac{m_x^2}{4\pi^2}+O(1).
\tag{24}
\]

Thus

\[
g_x
=
\frac{5m_x^2}{16\sqrt2\,\pi^2}+O(1),
\tag{25}
\]

while

\[
2D_x=\frac{5m_x^2-1}{3}.
\tag{26}
\]

Taking the limit in (1) gives (2):

\[
\frac{g_x}{2D_x}
\longrightarrow
\frac{3}{16\sqrt2\,\pi^2}.
\tag{27}
\]

This closes the strongest interpretation of the visual near-locking. The top band may remain *very* close to the matching subspace at every sampled level and still fail to converge to it in operator norm. The obstruction is small in constant size, but it is non-vanishing.

## 5. Average locking has a weaker logarithmic obstruction

For equal-rank orthogonal projectors of rank \(E_x\),

\[
\|P_x-Q_x\|_F^2
=
2E_x-2\operatorname{tr}(P_xQ_x)
=
2E_x(1-C_x).
\tag{28}
\]

From the Frobenius form of (19)--(21),

\[
\sqrt2\,\|B_x\|_F
\le
2D_x\|P_x-Q_x\|_F.
\tag{29}
\]

Together with (16) and (28),

\[
1-C_x
\ge
\frac{\|B_x\|_F^2}{4E_xD_x^2}
\ge
\frac{M_x}{E_x}\frac{g_x^2}{4D_x^2},
\]

which is (3).

The exact CRT ratio is

\[
\frac{M_x}{E_x}
=
\frac13
\prod_{7\le p\le x}\frac{p-3}{p-2}
=
\frac13
\prod_{7\le p\le x}
\left(1-\frac1{p-2}\right).
\tag{30}
\]

Since

\[
\log\left(1-\frac1{p-2}\right)
=
-\frac1p+O\left(\frac1{p^2}\right),
\tag{31}
\]

Mertens' reciprocal-prime theorem

\[
\sum_{p\le x}\frac1p
=
\log\log x+B+o(1)
\tag{32}
\]

implies (4). Separately, (25)--(26) give (5). Equations (3)--(5) prove the rate floor (6).

This explains why average and worst-angle behavior need not agree. The witness family has positive but slowly shrinking density inside the full matching basis. A sparse enough set of persistently rotated directions can keep the largest principal angle bounded away from zero while contributing only \(O(1/\log x)\) to the normalized Frobenius defect.

## 6. Numerical and visual consistency check

The retained visualization
[gap-two worst/average separation](../visualizations/gap2-locking-worst-average-separation.md)
plots the exact bounds above together with the already reproducible diagonalizations at the first three primorial stages.

For \(x=5,7,11\), the observed operator distances

\[
\|P_x-Q_x\|
\]

are approximately

\[
0.07838,\qquad0.08940,\qquad0.10064,
\]

while the observed average defects

\[
1-C_x
\]

are approximately

\[
0.003656,\qquad0.003701,\qquad0.003550.
\]

The exact bound (1) is much weaker numerically, already near its limiting value \(0.01343\). The exact Frobenius bound (3) is weaker still because it uses only the explicitly countable CRT witness family. This gap is useful: the theorem certifies a nonzero residual without pretending that the chosen local motif explains all of the finite spectral rotation.

The picture is diagnostic only. The mathematical conclusions (1)--(6) do not use the plotted samples.

## 7. Prior art and novelty boundary

The general language of invariant-subspace angles and perturbation bounds is classical. Chandler Davis and W. M. Kahan, **The Rotation of Eigenvectors by a Perturbation. III**, *SIAM Journal on Numerical Analysis* 7:1 (1970), 1--46, DOI `10.1137/0707001`, is the standard reference point. No new general matrix-perturbation theorem is claimed here; the commutator inequality (21) is elementary.

The prime-product estimate is likewise classical. Franz Mertens, **Ein Beitrag zur analytischen Zahlentheorie**, *Journal für die reine und angewandte Mathematik* 78 (1874), 46--62, DOI `10.1515/crll.1874.78.46`, supplies the reciprocal-prime asymptotic used in (32). Replacing \(1/p\) by \(1/(p-2)\) changes the logarithm of the product only by a convergent \(O(\sum p^{-2})\) correction.

The arithmetic input specific to this finding is the CRT witness (7)--(11) inside the primitive inverse-square chord operator of `PC-142`, together with the exact leakage coefficient (13). A targeted prior-art check did not identify this particular reduced-residue/gap-two projector application in the standard perturbation literature. That absence is not a historical-priority claim.

Nothing here is an RH criterion. `PC-142` already shows that the spectral-band cardinality and separation are controlled by local modulo-six structure. `VIS-005` sharpens that classicalization boundary: even the failure of perfect eigenspace locking is forced by a short CRT constellation and inverse-square chord weights.

## 8. Boundary conditions and falsification

The theorem concerns primorials \(N_x\) with \(x\ge5\). The CRT construction uses the primes \(2,3,5\) to force the local membership pattern and the primes \(p\ge7\) only through the exclusions in (8).

The strongest conclusion is specifically about operator norm, equivalently the worst principal angle. It does not say that a positive proportion of all matching directions remains strongly rotated, and it does not rule out \(C_x\to1\). The average result is only the lower rate bound (6).

The constant in (2) is not asserted to be sharp. It combines one local coefficient with the deliberately coarse global norm bound inherited from the period-six domination in `PC-142`. Stronger local constellations or sharper control of \(\|L_x\|\) could raise it.

The exact argument can be falsified at finite level without relying on a visualization:

1. enumerate the CRT class (7)--(8) and verify the count (11);
2. verify that \(a,a+2,a-4\) are primitive while \(a-2,a-6\) are not;
3. evaluate the two off-diagonal chord weights to check (13);
4. form \(B_x=(I-Q_x)L_xQ_x\) and verify (16);
5. check the commutator block identity (18), the projector identities, and the `PC-142` norm bound (22);
6. compare any exact diagonalization with (1) and (3).

A failure of any one of these exact statements would invalidate the corresponding bound.

## Consequence for the research line

The first visual spectral-locking experiment exposed two questions that looked almost identical at finite \(N\): whether the entire top band converges to the gap-two matching space, and whether almost all of that band does so on average. They are now mathematically separated.

The **worst-angle branch is closed negatively**: local CRT leakage forces a nonzero limiting projector distance. The **average branch remains open**, but this witness family imposes a logarithmic floor on its defect. Future visual work should therefore stop treating a single near-unity overlap statistic as evidence for full subspace identification. The more discriminating target is the distribution of principal angles and its decomposition by exact local CRT constellations.

For Prime Circle, this sharpens the accepted `CLUE-gap2-tail-eigenspace-locking`: the exact cliff from `PC-142` does not upgrade to uniform eigenspace convergence. Any surviving global arithmetic structure in the isolated band must be sought in the averaged angle profile, finer internal spacings, or cross-level transport after the local constellation effects are factored out.
