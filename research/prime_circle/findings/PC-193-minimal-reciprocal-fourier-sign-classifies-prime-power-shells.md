# PC-193 — minimal reciprocal Fourier sign classifies prime-power shells

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the minimally renormalized reciprocal amplitude at exponent one.

For `n>1`, define the even radial amplitude

\[
G_n(x):=\Phi_n(e^{-|x|})^{-1}-1,
\qquad x\in\mathbb R.
\tag{1}
\]

Then the real Fourier sign has an exact arithmetic dichotomy:

\[
\boxed{
 n=p^k\text{ for some prime }p
 \quad\Longleftrightarrow\quad
 \widehat G_n(t)<0\text{ for every }t\in\mathbb R.
}
\tag{2}
\]

Equivalently, among all shells `n>1`, the minimally renormalized reciprocal amplitude has **no real Fourier zero exactly on prime-power shells**. For every non-prime-power shell, PC-192 already proves that `widehat G_n` is positive somewhere, has a universal negative high-frequency tail, and therefore has a nonzero real zero.

The new content is the missing prime-power half of the classification. It follows from the exact prime-power cyclotomic factorization together with the same classical strip-Poisson Fourier kernel used in PC-191. The resulting criterion is a harmonic repackaging of prime-power structure, not a new RH mechanism: it distinguishes the von-Mangoldt support class `p^k`, not Riemann zero ordinates or the critical line.

## 1. Prime powers reduce exactly to the prime shell

Let `n=p^k`, `k>=1`, and put `a=p^{k-1}`. The standard cyclotomic identity

\[
\Phi_{p^k}(z)=\Phi_p(z^a)
\tag{3}
\]

gives immediately

\[
G_{p^k}(x)=G_p(ax).
\tag{4}
\]

Hence Fourier scaling yields

\[
\widehat G_{p^k}(t)
=\frac1a\widehat G_p\!\left(\frac{t}{a}\right).
\tag{5}
\]

It is therefore enough to determine the sign for one prime level `p`.

## 2. The prime-shell defect factors into two positive-definite kernels

For `q=e^{-|x|}` and prime `p`,

\[
\Phi_p(q)=\frac{1-q^p}{1-q}.
\tag{6}
\]

Thus

\[
G_p(x)
=\frac{1-q}{1-q^p}-1
=-\frac{q-q^p}{1-q^p}.
\tag{7}
\]

Set

\[
H_p(x):=-G_p(x)>0.
\tag{8}
\]

Writing `y=|x|`, elementary hyperbolic algebra gives the exact factorization

\[
\boxed{
H_p(x)
=e^{-y/2}
\frac{\sinh((p-1)y/2)}{\sinh(py/2)}.
}
\tag{9}
\]

The first factor has the strictly positive Fourier transform

\[
\widehat{e^{-|x|/2}}(t)
=\frac{1}{t^2+1/4}>0.
\tag{10}
\]

The second factor is also a strictly Fourier-positive kernel. This can be read directly from the strip-Poisson transform already used in PC-191. For

\[
g_\theta(u):=\frac1{2(\cosh u-\cos\theta)},
\qquad 0<\theta<\pi,
\tag{11}
\]

the classical formula is

\[
\widehat g_\theta(s)
=\frac{\pi}{\sin\theta}
\frac{\sinh((\pi-\theta)s)}{\sinh(\pi s)}.
\tag{12}
\]

Choose

\[
\theta=\frac\pi p,
\qquad
c=\frac{p}{2\pi}.
\tag{13}
\]

Then

\[
R_p(x):=
\frac{\sinh((p-1)x/2)}{\sinh(px/2)}
=\frac{\sin\theta}{\pi}\,\widehat g_\theta(cx),
\tag{14}
\]

with the removable value `R_p(0)=(p-1)/p`. Since `g_theta` is strictly positive, (14) already identifies `R_p` as a positive-definite function. Applying Fourier involution and scaling to (12) gives the stronger explicit formula

\[
\boxed{
\widehat R_p(t)
=\frac{2\pi\sin(\pi/p)}
{p\,[\cosh(2\pi t/p)-\cos(\pi/p)]}
>0
\qquad(t\in\mathbb R).
}
\tag{15}
\]

The formula includes `p=2`; no exceptional shell is needed.

## 3. Convolution makes the prime-power sign strict at every frequency

Equation (9) is the pointwise product

\[
H_p=E\,R_p,
\qquad
E(x):=e^{-|x|/2}.
\tag{16}
\]

Both factors are integrable, and (10), (15) are strictly positive everywhere. Therefore the product/convolution theorem gives

\[
\widehat H_p(t)
=\frac1{2\pi}
(\widehat E*\widehat R_p)(t)>0
\qquad(t\in\mathbb R).
\tag{17}
\]

Consequently

\[
\boxed{
\widehat G_p(t)<0
\qquad(t\in\mathbb R),
}
\tag{18}
\]

and (5) propagates the same strict sign to every prime power:

\[
\boxed{
\widehat G_{p^k}(t)<0
\qquad(k>=1,\ t\in\mathbb R).
}
\tag{19}
\]

No limiting argument, numerical observation, or RH assumption is involved.

## 4. PC-192 supplies the converse on every non-prime-power shell

PC-192 treats the more general family

\[
G_{n,\alpha}(x)
=\Phi_n(e^{-|x|})^{-\alpha}-1,
\qquad \alpha>0,
\tag{20}
\]

and proves that when `n>1` is not a prime power,

\[
\widehat G_{n,\alpha}(t)
=-\frac{\alpha\varphi(n)}{t^2}+o(t^{-2})
\qquad(|t|\to\infty),
\tag{21}
\]

while `G_{n,alpha}(0)=0` forces zero total Fourier mass. Hence the transform is positive somewhere before entering its negative tail and has a nonzero real zero.

Taking `alpha=1` and combining with (19) proves (2). In particular,

\[
\boxed{
 n\text{ is not a prime power}
 \quad\Longleftrightarrow\quad
 \widehat G_n\text{ changes sign and has a nonzero real zero}.
}
\tag{22}
\]

Thus the zero-existence question left open by PC-192 is completely classified at exponent one.

## 5. Prior-art and novelty audit

Every ingredient of the proof is classical. The identities (3) and (6) are standard cyclotomic formulas. The strip-Poisson transform (12) is the same classical potential-theory formula already anchored in `SOURCES.md` for PC-191 through Corso's Appendix B and Widder's strip harmonic theory. Fourier scaling, involution, and the product/convolution theorem are standard.

Directed searches for reciprocal cyclotomic amplitudes `Phi_p(e^{-x})^{-1}`, Fourier transforms combined with prime-power cyclotomic shells, and the equivalent hyperbolic-sine ratio did not locate a source presenting (2) as a number-theoretic or RH criterion. That absence is **not** treated as a novelty claim. Equation (2) is best understood as a Prime-Circle classification obtained by combining classical structures already present in the line.

The arithmetic information is also not mysterious. At the anchor,

\[
G_n(0)=\Phi_n(1)^{-1}-1,
\tag{23}
\]

and the classical identity

\[
\Phi_n(1)=
\begin{cases}
p,&n=p^k,\\
1,&n>1\text{ not a prime power}
\end{cases}
\tag{24}
\]

already separates the same two classes. The global Fourier sign theorem shows that this endpoint distinction extends rigidly across every frequency for `alpha=1`; it does not introduce a second arithmetic carrier.

## 6. Boundary conditions and what remains open

The result is deliberately limited to the reciprocal exponent `alpha=1`. PC-192 proves the non-prime-power zero statement for every real `alpha>0`, but the prime-power factorization (9) does not by itself show strict Fourier negativity of

\[
\Phi_{p^k}(e^{-|x|})^{-\alpha}-1
\]

for arbitrary non-integer `alpha`. No claim about that larger family is made here.

Nor does (2) locate any Fourier zero on a zeta scale, create a complex spectral parameter, generate the gamma factor, or produce an `s <-> 1-s` functional equation. It is a single-shell scalar criterion whose arithmetic content is exactly prime-power support. In particular, it cannot by itself distinguish primes from higher prime powers and does not supply an RH-strength implication.

The result also leaves untouched signed cross-shell combinations, shell-dependent matrix kernels, genuinely nonlocal angular/radial coupling, all-shell limits, singular boundary operators, and global uniformization/monodromy.

## 7. Audit checks

The claim has short independent falsifiers:

- verify (3) and the Fourier scaling (5);
- for a prime `p`, derive (7) directly from `Phi_p(q)=(1-q^p)/(1-q)`;
- check the exponential factor in (9), especially the surviving `e^{-|x|/2}`;
- substitute `theta=pi/p` and `c=p/(2pi)` into the strip-Poisson formula (12) and recover (14);
- apply Fourier involution to obtain the exact positive density (15);
- any prime power `p^k` and real frequency `t` with `widehat G_{p^k}(t)>=0` would falsify the new half of the theorem;
- any non-prime-power shell with no nonzero real zero would contradict PC-192 and therefore the converse in (22).

## Research consequence

PC-191 and PC-192 left two opposite scalar completions: the inversion-even raw reciprocal completion is Fourier-positive for every shell, while minimal subtraction manufactures Fourier zeros on every non-prime-power shell. PC-193 completes the exponent-one version of the latter picture: **minimal subtraction is not merely anti-selective on composites; its real Fourier sign is exactly a prime-power classifier.**

That classification is mathematically rigid but still classical in information content. A surviving spectral route cannot treat either positivity or real-zero existence of one fixed reciprocal shell as evidence toward RH. It must extract a source-forced quantitative relation among zero locations, couple shells before scalarization, or introduce genuinely nonlocal/global structure carrying information beyond the endpoint prime-power dichotomy.
