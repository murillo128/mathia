# PC-140 — primitive-shell Hessian trace classicalizes to Artin × Nicolas

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-RH-EQUIVALENCE` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY`. PC-136 derived the exact trace of every within-shell inverse-square chord Laplacian and the all-divisor trace defect of the canonical cross-shell resultant Hessian. PC-137 then showed that the **total** primorial trace/Wasserstein defect carries an RH-equivalent inequality which is exactly Nicolas' classical primorial totient criterion. PC-139 proved that the same defect nevertheless has a mesoscopic family of order-`N^2` modes already inside the primitive shell.

The remaining first-moment question can be answered exactly. On the primorial common refinement, the trace contributed by the **top primitive shell alone** is a positive asymptotic fraction of the entire omitted within-shell trace. However, its arithmetic normalization factors as the square of the primorial totient product times the finite Euler product converging to **Artin's constant**. Consequently the natural RH criterion obtained from this primitive-shell trace is again literally Nicolas' criterion, not a new spectral mechanism.

Thus the primitive shell is not negligible: it carries about `44.6%` of the total defect trace asymptotically. But at the scalar first-moment level that substantial spectral mass is already completely classicalized. Any surviving information must lie in how the primitive-shell modes are organized, not in their total energy.

## 1. Start from the exact primitive-shell trace of PC-136

Let

\[
N_x:=\prod_{p\le x}p
\]

be the primorial common refinement and let

\[
T_x:=\operatorname{tr}L_{N_x}^{\rm int}
\]

be the trace of the inverse-square chord Laplacian using only edges whose two endpoints lie in the top exact-order shell

\[
P_{N_x}^*=U(N_x).
\]

PC-136 proved, for every `n`,

\[
\operatorname{tr}L_n^{\rm int}
=\frac1{12}
\left[
 n^3\prod_{p\mid n}
 \left(1-\frac2p+\frac1{p^3}\right)
 -\varphi(n)
\right].
\]

Therefore

\[
\boxed{
12T_x+\varphi(N_x)
=N_x^3
\prod_{p\le x}
\left(1-\frac2p+\frac1{p^3}\right).
}
\tag{1}
\]

The local factor has the elementary factorization

\[
\boxed{
1-\frac2p+\frac1{p^3}
=\left(1-\frac1p\right)^2
\left(1-\frac1{p(p-1)}\right).
}
\tag{2}
\]

Define the finite Artin product

\[
A_x:=\prod_{p\le x}
\left(1-\frac1{p(p-1)}\right).
\tag{3}
\]

Using

\[
\frac{\varphi(N_x)}{N_x}
=\prod_{p\le x}\left(1-\frac1p\right),
\]

equations (1)--(3) give the exact identity

\[
\boxed{
\frac{12T_x+\varphi(N_x)}{N_x^3}
=A_x
\left(\frac{\varphi(N_x)}{N_x}\right)^2.
}
\tag{4}
\]

This is the load-bearing classification. The primitive-shell first moment contains no new Euler product beyond the classical totient factor and the standard Artin product.

## 2. The asymptotic constant is exactly Artin's constant

The factors in (3) differ from one by `O(p^{-2})`, so

\[
A_x\longrightarrow
A:=\prod_p
\left(1-\frac1{p(p-1)}\right)
=0.3739558136\ldots,
\tag{5}
\]

where `A` is Artin's constant from the classical primitive-root conjecture. Combining (4) with Mertens' prime-product theorem gives

\[
\boxed{
\frac{T_x}{N_x^3}
\sim
\frac{A e^{-2\gamma}}{12(\log x)^2}.
}
\tag{6}
\]

The appearance of `A` here must not be confused with a new primitive-root theorem. It comes from the elementary local factorization (2) of the already-derived PC-136 shell trace. No statement about an integer being a primitive root modulo primes is used.

There is nevertheless a useful structural message: the top exact-order shell contributes at the same Mertens-squared scale as the whole primorial Hessian defect, rather than becoming lower order.

## 3. The primitive shell carries a fixed positive fraction of the total defect trace

Write

\[
\Delta_x
:=\operatorname{tr}(L_{N_x}-H_{N_x}^{\times})
\]

for the total omitted within-shell trace. PC-136 gives

\[
12\Delta_x+N_x
=N_x^3
\prod_{p\le x}
\left(1-\frac2p+\frac2{p^3}\right).
\tag{7}
\]

PC-137 factors the second local product as

\[
1-\frac2p+\frac2{p^3}
=\left(1-\frac1p\right)^2 q_p,
\qquad
q_p:=1-\frac{p-2}{p(p-1)^2},
\tag{8}
\]

and therefore, with

\[
Q_x:=\prod_{p\le x}q_p,
\qquad
C:=\prod_p q_p>0,
\tag{9}
\]

one has

\[
\frac{12\Delta_x+N_x}{N_x^3}
=Q_x
\left(\frac{\varphi(N_x)}{N_x}\right)^2.
\tag{10}
\]

Dividing the exact formulas rather than only their asymptotics gives

\[
\boxed{
\frac{T_x}{\Delta_x}
=
\frac{
A_x-\dfrac1{N_x\varphi(N_x)}
}{
Q_x-\dfrac1{\varphi(N_x)^2}
}.
}
\tag{11}
\]

Hence

\[
\boxed{
\frac{T_x}{\Delta_x}
\longrightarrow
\frac{A}{C}
=\prod_p
\frac{1-\dfrac1{p(p-1)}}
{1-\dfrac{p-2}{p(p-1)^2}}
\approx0.44588.
}
\tag{12}
\]

The product in (12) converges absolutely because each local ratio is `1+O(p^{-3})`. Thus approximately `44.6%` of the **trace**, not merely a vanishing exceptional correction, is asymptotically carried by the primitive shell alone.

Finite controls show the convergence immediately:

\[
\frac{T_6}{\Delta_6}=\frac12,
\qquad
\frac{T_{30}}{\Delta_{30}}=\frac{47}{104}\approx0.451923,
\qquad
\frac{T_{210}}{\Delta_{210}}
=\frac{5841}{13069}\approx0.446935.
\tag{13}
\]

This sharpens the location statement behind PC-139. The guaranteed gap-two macroscopic modes found there already live in the primitive block; (12) now shows that the entire primitive block also carries a nonzero limiting fraction of the first spectral moment of the defect.

## 4. The natural primitive-shell RH criterion is exactly Nicolas again

Equation (4) gives a tempting RH-sensitive scalar because the only slowly varying factor is the primorial totient product. Define

\[
\mathcal A_x
:=
\frac{e^{2\gamma}(\log\log N_x)^2}{A_x}
\frac{12T_x+\varphi(N_x)}{N_x^3}.
\tag{14}
\]

Then there is no approximation:

\[
\boxed{
\mathcal A_x
=
\left[
 e^\gamma\log\log N_x
 \frac{\varphi(N_x)}{N_x}
\right]^2.
}
\tag{15}
\]

The bracket is exactly the Nicolas function at the prime endpoint `x=p_k` used in PC-137. Therefore Nicolas' classical theorem gives

\[
\boxed{
\mathrm{RH}
\iff
\mathcal A_{p_k}<1
\quad\text{for every }p_k>2.
}
\tag{16}
\]

Equation (15) simultaneously proves why (16) is **not** a new Prime-Circle RH criterion in the mechanism sense. The primitive-shell trace contributes the finite Artin factor `A_x`, but once that elementary absolutely convergent correction is removed, the purported spectral criterion is literally the square of the same classical primorial totient quantity already isolated by PC-137.

Thus the information flow is

\[
\boxed{
T_x
\longleftrightarrow
A_x\left(\frac{\varphi(N_x)}{N_x}\right)^2
\longrightarrow
\text{Nicolas criterion}.
}
\tag{17}
\]

There is no independent spectral parameter, functional equation, gamma factor, critical-line involution, or zero divisor generated by the trace.

## 5. Relation to the PC-139 mesoscopic tail

PC-139 found a different scalar statistic in the same primitive shell. The number of disjoint gap-two primitive pairs is

\[
E_x=\prod_{3\le p\le x}(p-2),
\]

with exact normalization

\[
\frac{E_x}{N_x}
=2C_{2,x}
\left(\frac{\varphi(N_x)}{N_x}\right)^2,
\]

where `C_{2,x}` tends to the classical twin-prime singular factor. The present result shows that the **entire primitive-shell trace** has the parallel form

\[
\frac{12T_x+\varphi(N_x)}{N_x^3}
=A_x
\left(\frac{\varphi(N_x)}{N_x}\right)^2.
\]

So two quite different primitive-shell observables now have the same information pattern:

\[
\text{local classical sieve product}
\times
\left(\frac{\varphi(N_x)}{N_x}\right)^2.
\]

For the guaranteed macroscopic-mode count the local factor is the prime-pair/twin-prime product; for the complete first moment it is Artin's product. In both cases the slowly varying RH-sensitive core is the same Mertens/Nicolas totient product.

This is a stronger novelty warning than merely saying that both quantities have size `Theta((log x)^{-2})`. Their exact finite arithmetic separates into a standard local admissibility product and the same squared totient factor. Scalar renormalizations of either observable therefore risk only repackaging classical prime-product criteria.

## 6. Prior-art and novelty audit

No theorem-level historical novelty is claimed for the ingredients or for Artin's constant. The exact shell-trace formula is already persisted in PC-136 and ultimately comes from the classical `csc^2` regular-polygon identity plus CRT counting. The product

\[
\prod_p\left(1-\frac1{p(p-1)}\right)
\]

is the standard Artin constant. A modern authoritative survey is Pieter Moree, **Artin's Primitive Root Conjecture — A Survey**, *Integers* 12:6 (2012), 1305–1416, DOI `10.1515/integers-2012-0043`; the classical conditional proof of Artin's conjecture under GRH is Christopher Hooley, **On Artin's conjecture**, *Journal für die reine und angewandte Mathematik* 225 (1967), 209–220, DOI `10.1515/crll.1967.225.209`.

The RH equivalence in (16) is not claimed independently: PC-137 already audited the Nicolas theorem and established that the corresponding total-Hessian defect criterion is exactly Nicolas. Equation (15) shows that the primitive-shell specialization lands on precisely the same classical function.

Directed searches across Artin's constant, reduced-residue cosecant sums, roots-of-unity Laplacians, primitive-shell Riesz energies, and related spectral language did not expose this exact Prime-Circle linkage. That absence is not evidence of priority. The durable contribution is the research boundary: **a spectrally substantial top-shell component survives the bulk collapse, but its complete first moment factorizes into Artin's classical local product times Nicolas' classical RH-sensitive totient product.**

## 7. Falsification surface and surviving scope

The claim has several exact controls.

1. At every primorial `N_x`, direct construction of the primitive-shell inverse-square Laplacian must satisfy (4). For `N=6`, `T_6=2/3`; for `N=30`, `T_{30}=188/3`; for `N=210`, `T_{210}=15576`.
2. The local factorization (2) must hold prime by prime. Any discrepancy would destroy the Artin identification.
3. The exact ratio (11) must agree with direct traces of the primitive block and the all-divisor defect. The values in (13) provide finite nontrivial checks.
4. The Nicolas normalization (15) is an algebraic identity, not an asymptotic claim. If a proposed RH criterion from `T_x` uses only `A_x`, `N_x`, and elementary normalization, it must be checked against this exact collapse before being counted as new.

The conclusion is deliberately limited to the **first spectral moment**. It does not determine the primitive-shell eigenvalue distribution, eigenvector localization, correlations among distinct short-gap patterns, higher centered moments, second/top-nearby eigenvalues of `H_{N_x}^{\times}`, or cross-level transport of the mesoscopic modes. PC-139 already proves that order-`N_x^2` defect modes survive, and (12) shows that the primitive shell carries a large amount of total energy; neither fact says that the detailed mode organization is classical.

The research frontier is therefore narrower but still genuine: a new RH mechanism would have to use information in the **shape, organization, or dynamics** of the surviving primitive-shell/edge modes that is lost under trace. The trace itself has now been fully classicalized to Artin × Nicolas.