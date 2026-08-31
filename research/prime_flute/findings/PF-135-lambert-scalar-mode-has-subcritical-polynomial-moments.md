# PF-135 — Lambert scalar mode has subcritical polynomial moments

**Status:** `EXACT-DERIVED + LITERATURE-BACKED + NEGATIVE/BOUNDARY`. PF-132 isolates the exact full split-ray scalar mismatch

\[
c_n=\beta_n-\beta_{n+1},
\]

PF-133 shows that it is the only nonintegrable deep-cusp mode of the PF-121 trace, and PF-134 proves the logarithmically weighted estimate `sum (log p_n)|c_n|<infinity`. The present calculation strengthens that arithmetic budget from one logarithm to a genuine polynomial range. Using only the source-audited Baker--Harman--Pintz short-interval exponent `0.525`, one has

\[
\boxed{
\sum_n p_n^\alpha |c_n|<\infty
\qquad\text{for every }0\le\alpha<\frac{19}{40}=0.475.
}
\]

As a geometric corollary, the square-root aspect factor between two adjacent Lambert halves is summable against `|c_n|`: if `A_n=cosh(a_n)`, then

\[
\kappa_n:=
\left(\frac{\max(A_n,A_{n+1})}{\min(A_n,A_{n+1})}\right)^{1/2}
\ll p_n^{21/80},
\qquad
\sum_n \kappa_n|c_n|<\infty.
\]

This removes a specific extreme-neighboring-gap amplification from the accepted wave-operator program: in the Fermi corridor between the two Lambert corner heights, the reciprocal of the **combined** transverse width grows by at most this square-root aspect factor, so the scalar mismatch still has finite total budget there. It does **not** construct a boundary-coherent two-dimensional comparison, control the long pre-first-corner narrow region, prove the Güneysu--Thalmaier inverse-unit-ball integral, establish wave operators, or imply any RH statement.

## Claim

Use PF-114/PF-134 notation

\[
h_n=F(p_{n+1})-F(p_n),
\qquad
h_n^+=F(p_{n+1}+1)-F(p_n+1),
\qquad
F(x)=\log\cot\frac{\pi}{x},
\tag{1}
\]

\[
R_n=\frac{h_n^+}{h_n},
\qquad
d_n=\log R_n<0,
\qquad
q_n:=-d_n>0,
\tag{2}
\]

and

\[
\varepsilon_n
=\log\frac{\cosh a_n^+}{\cosh a_n},
\qquad
\beta_n
=\log\frac{\sinh a_n^+}{\sinh a_n},
\qquad
c_n=\beta_n-\beta_{n+1}.
\tag{3}
\]

PF-114 proves on a tail that `q_n` is decreasing to zero and

\[
q_n\le \frac{C}{p_n}.
\tag{4}
\]

PF-119/PF-134 give the exact decomposition

\[
\varepsilon_n=-d_n+r_n=q_n+r_n,
\qquad
r_n=E(h_n^+)-E(h_n),
\qquad
|r_n|\le C h_n^2,
\tag{5}
\]

where `E(h)=h^2/12+O(h^4)`, and PF-132 gives

\[
s_n:=\beta_n-\varepsilon_n
=\log\frac{\tanh a_n^+}{\tanh a_n},
\qquad
|s_n|\le C h_n^2
\tag{6}
\]

on a sufficiently far tail. Then for every

\[
0\le\alpha<\frac{19}{40},
\tag{7}
\]

one has

\[
\boxed{
\sum_n p_n^\alpha |c_n|<\infty.
}
\tag{8}
\]

Moreover, write

\[
A_n:=\cosh a_n=\coth\frac{h_n}{2}.
\tag{9}
\]

Then

\[
\boxed{
\kappa_n
:=
\left(
\frac{\max(A_n,A_{n+1})}
     {\min(A_n,A_{n+1})}
\right)^{1/2}
\ll p_n^{21/80},
}
\tag{10}
\]

and consequently

\[
\boxed{
\sum_n\kappa_n|c_n|<\infty.
}
\tag{11}
\]

Finally consider the two PF-125/PF-131 Lambert Fermi widths `H_{a_n}(tau)` and `H_{a_{n+1}}(tau)` in the common physical split-ray Busemann coordinate. If, say, `A_n<=A_{n+1}` and `T_{a_n}<=tau<=T_{a_{n+1}}`, their exact branch formulas imply

\[
\tanh H_{a_n}(\tau)=A_n e^{-\tau},
\qquad
\tanh H_{a_{n+1}}(\tau)
=\frac{\cosh\tau}{A_{n+1}}
\ge \frac{e^\tau}{2A_{n+1}}.
\tag{12}
\]

Hence

\[
\boxed{
H_{a_n}(\tau)+H_{a_{n+1}}(\tau)
\ge
\sqrt{\frac{2A_n}{A_{n+1}}},
}
\tag{13}
\]

with the symmetric statement if the order is reversed. Thus the reciprocal combined width on the interval between the two Lambert corner heights is `O(kappa_n)`, and (11) proves that this natural square-root aspect amplification cannot make the scalar trace mode nonsummable.

## 1. The monotone shift factor has every polynomial moment below one

PF-114 proves that `q_n=-d_n` decreases to zero. For `0<alpha<1`, put

\[
w_n=p_n^\alpha.
\]

Discrete summation by parts gives, for `M>N`,

\[
\sum_{n=N}^{M}w_n(q_n-q_{n+1})
=
w_Nq_N
+\sum_{n=N+1}^{M}q_n(w_n-w_{n-1})
-w_Mq_{M+1}.
\tag{14}
\]

The boundary term tends to zero by (4), because

\[
w_Mq_{M+1}\le C p_M^{\alpha-1}\to0.
\tag{15}
\]

For the interior term, the mean-value theorem and monotonicity of `x^(alpha-1)` give

\[
w_n-w_{n-1}
\le C_\alpha (p_n-p_{n-1})p_{n-1}^{\alpha-1}.
\tag{16}
\]

Together with `q_n<=C/p_n<=C/p_{n-1}`,

\[
q_n(w_n-w_{n-1})
\le
C_\alpha (p_n-p_{n-1})p_{n-1}^{\alpha-2}.
\tag{17}
\]

Since `alpha-2<-1`, the prime intervals partition the tail and Bertrand makes the decreasing integrand uniformly comparable on each interval, so

\[
\sum_n(p_n-p_{n-1})p_{n-1}^{\alpha-2}
\ll
\int^\infty x^{\alpha-2}\,dx
<\infty.
\tag{18}
\]

Therefore

\[
\boxed{
\sum_n p_n^\alpha|d_{n+1}-d_n|<\infty
\qquad(0\le\alpha<1).
}
\tag{19}
\]

The reciprocal-prime common mode is therefore substantially better after the adjacent difference than the logarithmic estimate of PF-134 alone reveals.

## 2. The regular collar remainder fixes the unconditional endpoint at `19/40`

The restriction in (8) comes from the regular `h_n^2` remainder, not from the monotone shift factor. The source-audited Baker--Harman--Pintz bound is

\[
g_n:=p_{n+1}-p_n\ll p_n^{21/40}.
\tag{20}
\]

PF-114 gives `h_n<<g_n/p_n`; hence

\[
h_n^2
\ll
\frac{g_n^2}{p_n^2}
\ll
g_n p_n^{-59/40}.
\tag{21}
\]

For `alpha<19/40`, the function

\[
x^{\alpha-59/40}
\]

has exponent strictly below `-1`. Therefore

\[
\sum_n p_n^\alpha h_n^2
\ll
\sum_n g_n p_n^{\alpha-59/40}
\ll
\int^\infty x^{\alpha-59/40}\,dx
<\infty.
\tag{22}
\]

Equations (5)--(6) imply

\[
\sum_n p_n^\alpha|r_n|<\infty,
\qquad
\sum_n p_n^\alpha|s_n|<\infty.
\tag{23}
\]

A one-index shift, using `p_{n+1}<2p_n`, gives the same bounds for the first differences of `r_n` and `s_n`.

Now

\[
\begin{aligned}
c_n
&=\beta_n-\beta_{n+1}\\
&=(q_n-q_{n+1})
 +(r_n-r_{n+1})
 +(s_n-s_{n+1}).
\end{aligned}
\tag{24}
\]

Combining (19) and (23) proves (8).

This also identifies exactly where the numerical exponent enters. Any future audited improvement `g_n<<p_n^theta` with `theta<1` upgrades the same proof to every

\[
\alpha<1-\theta.
\tag{25}
\]

A current arXiv preprint by Runbo Li (`arXiv:2308.04458`) states the stronger short-interval exponent `theta=0.52`; if that input is later promoted into the line's audited source set, the numerical endpoint in (8) becomes `alpha<0.48`. PF-135 deliberately keeps the boxed theorem on the already-audited Baker--Harman--Pintz input.

## 3. Extreme neighboring cuff aspect has only a square-root cost in the middle corridor

The exact derivative in PF-114 satisfies `f(t)asymp1/t` on the tail, so

\[
h_n\asymp\frac{g_n}{p_n}.
\tag{26}
\]

Since `h_n->0`, (9) gives

\[
A_n\asymp\frac1{h_n}\asymp\frac{p_n}{g_n}.
\tag{27}
\]

For adjacent indices, Bertrand makes `p_{n+1}asymp p_n`. Therefore

\[
\frac{A_{n+1}}{A_n}
\ll\frac{g_n}{g_{n+1}},
\qquad
\frac{A_n}{A_{n+1}}
\ll\frac{g_{n+1}}{g_n}.
\tag{28}
\]

Every odd-prime gap is at least `2`, while (20), one index shifted if necessary, gives both adjacent gaps `O(p_n^(21/40))`. Hence

\[
\frac{\max(A_n,A_{n+1})}{\min(A_n,A_{n+1})}
\ll p_n^{21/40},
\tag{29}
\]

which proves (10).

The exponent needed for the square root is

\[
\frac{21}{80}=0.2625
<
\frac{19}{40}=0.475.
\tag{30}
\]

Thus (8) with any fixed `alpha` strictly between these two numbers gives (11).

Equation (13) makes this more than a coordinate observation. Between the two corner heights, one Lambert half is on its outgoing cusp-side branch while the other is still on its incoming finite-cuff branch. The AM--GM inequality applied to (12) gives

\[
A_n e^{-\tau}
+
\frac{e^\tau}{2A_{n+1}}
\ge
\sqrt{\frac{2A_n}{A_{n+1}}}.
\tag{31}
\]

Since `H>=tanh H`, this is (13). Therefore an extension estimate that loses only the reciprocal **combined** transverse width in this middle corridor pays at worst `kappa_n`, and the scalar mismatch can absorb that loss absolutely over all pants.

## 4. What this closes and what it does not

PF-134 proved that a logarithmically growing Busemann propagation length cannot amplify `c_n` into divergence. PF-135 shows a stronger fact:

\[
\boxed{
\text{scalar Lambert mismatch}
\times
\text{any }p_n^\alpha\text{ loss with }\alpha<19/40
\in\ell^1.
}
\tag{32}
\]

In particular, the natural square-root aspect loss caused by extreme neighboring cuff ratios in the interval **between** the two Lambert corners is harmless. This removes one concrete candidate for the boundary-coherent failure of PF-130: an extreme prime-gap ratio cannot by itself create divergence merely through the middle-corridor width imbalance.

There remains a genuinely different region before the first Lambert corner. There both transverse widths can be of order `1/A_n` or `1/A_{n+1}`, much smaller than their square-root aspect scale, while the PF-121 trace has already entered its nontrivial tail after bounded Busemann height. A naive transverse correction there can therefore pay a factor as large as an individual `A_n`, and PF-135 does **not** prove that such a cost is summable. Nor does it prove that such a naive correction is necessary: PF-125 already shows that other boundary-coherent maps exist, albeit without PF-130's sharp strong-`L^1` localization.

Thus the accepted wave clue is narrowed to a more specific two-dimensional question: construct a comparison that combines PF-130's localized body cost with PF-125/PF-129 boundary coherence **without paying an individual large-cuff factor through the long pre-corner corridor**, and then control the ambient inverse-unit-ball weight on noncanonical thin regions.

## 5. Prior art and novelty audit

No novelty is claimed for discrete Abel/summation-by-parts estimates, the Baker--Harman--Pintz short-interval theorem, the collar asymptotic `coth(h/2)asymp1/h`, AM--GM, or elementary Fermi-coordinate width estimates. The general wave-operator target remains Güneysu--Thalmaier's inverse-unit-ball weighted criterion already audited in `SOURCES.md` and the accepted local clue.

Directed current-source checks also located Runbo Li's `arXiv:2308.04458`, whose current abstract states that `[x-x^0.52,x]` contains primes for all sufficiently large `x`. That is a potentially stronger arithmetic input, not a prime-flute spectral theorem, and is not needed for the durable claim above.

No source located states the project-specific combination (8), (11), or (13) for the cotangent prime/shift flute. The durable contribution is therefore the exact localization of the remaining amplification budget: the scalar trace mode has polynomially weighted finite mass far beyond the logarithmic cusp-entry scale, and the extreme **square-root** neighboring-cuff aspect in the middle Lambert corridor lies safely inside that budget. This is negative/boundary evidence for the all-composite control, not evidence for RH.

## 6. Audit / falsification core

A later adversary can verify PF-135 through the following finite chain:

1. import PF-114's monotonicity of `d_n`, set `q_n=-d_n`, and verify `q_n<=C/p_n`;
2. apply (14)--(18) to obtain the weighted first-difference estimate (19) for every `alpha<1`;
3. import PF-134's exact decompositions (5)--(6) and PF-114's `h_n<<g_n/p_n`;
4. use only the audited Baker--Harman--Pintz exponent `21/40` to obtain (21)--(23), with the endpoint `alpha<19/40`;
5. combine the three exact first-difference terms in (24) to obtain (8);
6. verify `h_nasymp g_n/p_n`, `A_n=coth(h_n/2)asymp1/h_n`, the adjacent aspect estimate (28), odd-prime gap lower bound, and BHP upper bound to obtain (10)--(11);
7. import PF-125's exact Lambert Fermi branches and check (12)--(13) by AM--GM;
8. do not extend (13) to the pre-first-corner region and do not infer a global metric, wave-operator, scattering, Schatten, determinant, or RH theorem.

A refutation must break one of these explicit weighted estimates or imported exact identities. Failure of the broader wave-operator program would not refute PF-135; it would identify a stronger amplification than the polynomial scalar/aspect mechanisms ruled out here.

## References

- R. C. Baker, G. Harman, J. Pintz, *The Difference Between Consecutive Primes, II*, Proc. London Math. Soc. 83 (2001), 532--562, DOI `10.1112/S0024611501012690`.
- R. Li, *The number of primes in short intervals and numerical calculations for Harman's sieve*, arXiv:2308.04458 (current source check only; not used in the boxed theorem).
- PF-114, PF-119, PF-125, PF-132, PF-133, and PF-134 in this research ledger.
