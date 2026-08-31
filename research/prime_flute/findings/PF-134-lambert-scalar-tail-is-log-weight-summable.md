# PF-134 — Lambert scalar tail is log-weight summable

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. PF-132 isolates the exact adjacent Lambert split-ray scalar mismatch `c_n=beta_n-beta_{n+1}` and proves `c in ell^1`; PF-133 shows that after subtracting this scalar mode the entire deep-cusp trace residual is summable in strong `W^{1,1}`. A remaining trace-level loophole was that the scalar correction might have to be transported across a **growing pre-cusp Busemann interval** before PF-129's fixed-height cusp synchronization can take over, potentially multiplying `|c_n|` by a length of order `log p_n`. The exact shift-clone mesh estimates rule this out:

\[
\boxed{\sum_n (1+\log p_n)|c_n|<\infty.}
\]

Moreover, the canonical PF-119 cusp-split foot has Busemann height `T_n=O(log p_n)` relative to the standard horocycle, so `sum T_n|c_n|<infinity`. Thus logarithmic cusp-entry length does **not** resurrect a nonsummable scalar boundary mode. This remains a one-dimensional trace/boundary budget: no two-dimensional boundary-coherent extension, Güneysu--Thalmaier weighted metric criterion, wave operator, scattering equivalence, Schatten statement, determinant, or RH conclusion is claimed.

## Claim

Use the PF-114/PF-119 logarithmic meshes

\[
h_n=F(p_{n+1})-F(p_n),
\qquad
h_n^+=F(p_{n+1}+1)-F(p_n+1),
\qquad
F(x)=\log\cot\frac{\pi}{x},
\tag{1}
\]

and put

\[
R_n:=\frac{h_n^+}{h_n},
\qquad
d_n:=\log R_n.
\tag{2}
\]

PF-114 proves on a tail that

\[
d_n<d_{n+1}<0,
\qquad
d_n\to0,
\qquad
d_n=-\frac1{p_n}+o(p_n^{-1}).
\tag{3}
\]

Let

\[
a_n=\frac{\ell_n}{2},
\qquad
\varepsilon_n:=\log\cosh a_n^+-\log\cosh a_n,
\tag{4}
\]

and use PF-132's Lambert parameter

\[
\beta_n:=\log\frac{\sinh a_n^+}{\sinh a_n},
\qquad
c_n:=\beta_n-\beta_{n+1}.
\tag{5}
\]

Then

\[
\boxed{
\sum_n \log p_n\,|c_n|<\infty.
}
\tag{6}
\]

Next take the exact PF-119 upper-half-plane normalization of the one-cusp pant with adjacent half-cuffs `a_n,a_{n+1}`. Its central split ray meets the finite common perpendicular at Euclidean height

\[
R_n^{\rm cusp}
=\frac1{\cosh a_n+\cosh a_{n+1}}.
\tag{7}
\]

Measure Busemann height upward from that point to the standard horocycle `y=1`:

\[
T_n:=\log\frac1{R_n^{\rm cusp}}
=\log(\cosh a_n+\cosh a_{n+1}).
\tag{8}
\]

Then

\[
\boxed{T_n\le C+\log p_n}
\tag{9}
\]

on a tail, and therefore

\[
\boxed{
\sum_n T_n|c_n|<\infty.
}
\tag{10}
\]

As a trace-level corollary, a scalar interpolation of size `c_n` distributed across the whole interval of length `T_n` has a summable `L^1+\dot W^{1,1}` budget. Hence the growing distance from the canonical pant split to a fixed standard cusp horocycle is not by itself an obstruction to the accepted wave-operator program.

## 1. The monotone mesh shift has log-weighted finite variation

Set

\[
q_n:=-d_n>0,
\qquad
w_n:=\log p_n.
\tag{11}
\]

By (3), `q_n` decreases to zero. The asymptotic in (3) also gives, after increasing the tail index if necessary,

\[
q_n\le\frac{C}{p_n}.
\tag{12}
\]

For `M>N`, discrete summation by parts gives

\[
\sum_{n=N}^{M}w_n(q_n-q_{n+1})
=
w_Nq_N
+\sum_{n=N+1}^{M}q_n(w_n-w_{n-1})
-w_Mq_{M+1}.
\tag{13}
\]

Now

\[
w_n-w_{n-1}
=\log\frac{p_n}{p_{n-1}}
\le\frac{p_n-p_{n-1}}{p_{n-1}}.
\tag{14}
\]

Combining (12)--(14),

\[
q_n(w_n-w_{n-1})
\le
C\frac{p_n-p_{n-1}}{p_{n-1}p_n}
=
C\left(\frac1{p_{n-1}}-\frac1{p_n}\right).
\tag{15}
\]

The right side telescopes, while `w_Mq_{M+1}->0` because `log p_M/p_{M+1}->0`. Therefore

\[
\boxed{
\sum_n \log p_n\,|d_{n+1}-d_n|<\infty.
}
\tag{16}
\]

This strengthens PF-114's unweighted total-variation statement exactly by the logarithmic factor needed for a cusp-entry interval of length `O(log p_n)`.

## 2. The regular collar remainder also survives the logarithmic weight

PF-119 writes the exact collar scale as

\[
J(h):=\log\coth\frac h2
=\log\frac2h+E(h),
\qquad
E(h)=\frac{h^2}{12}+O(h^4),
\tag{17}
\]

so that

\[
\varepsilon_n=-d_n+r_n,
\qquad
r_n:=E(h_n^+)-E(h_n).
\tag{18}
\]

Because `0<h_n^+<h_n` on the tail,

\[
|r_n|\le C h_n^2.
\tag{19}
\]

PF-114 uses the unconditional Baker--Harman--Pintz gap bound `g_n:=p_{n+1}-p_n \ll p_n^{0.525}` together with `h_n\ll g_n/p_n` to obtain

\[
h_n^2\ll g_n p_n^{-1.475}.
\tag{20}
\]

The same estimate retains one logarithm. Indeed, for

\[
H(x):=(\log x)x^{-1.475},
\]

`H` is decreasing on a tail, and Bertrand's bound `p_{n+1}<2p_n` makes `H(x)` uniformly comparable to `H(p_n)` throughout each prime interval `[p_n,p_{n+1}]`. Hence

\[
\sum_n \log p_n\,h_n^2
\ll
\sum_n g_n H(p_n)
\ll
\int^\infty (\log x)x^{-1.475}\,dx
<\infty.
\tag{21}
\]

Thus

\[
\sum_n w_n|r_n|<\infty,
\qquad
\sum_n w_n|r_n-r_{n+1}|<\infty,
\tag{22}
\]

where the second statement follows by shifting one summation index and using `w_n<=w_{n+1}`. Equations (16), (18), and (22) yield

\[
\boxed{
\sum_n \log p_n\,|\varepsilon_n-\varepsilon_{n+1}|<\infty.
}
\tag{23}
\]

So the logarithmic cusp-length weight remains harmless even after restoring the exact regular part of the collar conversion.

## 3. Passing from the canonical cusp scale to the Lambert parameter

PF-132 compares the Lambert parameter `beta_n` with the PF-119 cusp-chart scale `epsilon_n` by

\[
s_n:=\beta_n-\varepsilon_n
=
\log\frac{\tanh a_n^+}{\tanh a_n}.
\tag{24}
\]

On the tail its proof gives

\[
|s_n|
\le
C|a_n^+-a_n|e^{-2a_n}.
\tag{25}
\]

PF-107 gives a bounded half-cuff displacement (in fact `a_n^+-a_n=O(1/p_n)`), while the exact collar identity

\[
\sinh a_n\,\sinh\frac{h_n}{2}=1
\tag{26}
\]

implies `e^{-2a_n}\le C h_n^2` for all sufficiently large `n`. By (21),

\[
\boxed{
\sum_n \log p_n\,|s_n|<\infty.
}
\tag{27}
\]

Finally

\[
\begin{aligned}
c_n
&=\beta_n-\beta_{n+1}\\
&=(\varepsilon_n-\varepsilon_{n+1})
 +(s_n-s_{n+1}),
\end{aligned}
\tag{28}
\]

and (23), (27), plus another one-index shift prove (6).

This step is important conceptually. PF-133's scalar `c_n` is not merely an abstract `ell^1` sequence: its exact prime/shift origin carries enough extra adjacent-cancellation structure to absorb one full logarithm of spatial propagation.

## 4. The canonical pre-cusp Busemann length is only logarithmic

It remains to verify that the geometrically relevant pre-cusp distance really has size at most `O(log p_n)`.

From PF-114,

\[
h_n
=
\int_{p_n}^{p_{n+1}}
\frac{2\pi}{t^2\sin(2\pi/t)}\,dt.
\tag{29}
\]

Since `sin u<=u` for positive `u`, the integrand is at least `1/t`. Therefore

\[
h_n
\ge
\log\frac{p_{n+1}}{p_n}
\ge
\frac{g_n}{p_{n+1}}
\ge
\frac2{p_{n+1}}
\tag{30}
\]

for the odd-prime tail. The exact collar conversion gives

\[
\cosh a_n
=
\coth\frac{h_n}{2}
=
1+\frac{2}{e^{h_n}-1}
\le
1+\frac2{h_n}
\le
1+p_{n+1}.
\tag{31}
\]

Applying the same estimate one index later and substituting into (8),

\[
T_n
\le
\log(2+p_{n+1}+p_{n+2}).
\tag{32}
\]

Bertrand's postulate twice gives `p_{n+1}<2p_n` and `p_{n+2}<4p_n`, so

\[
\boxed{
T_n\le\log(2+6p_n)\le C+\log p_n.
}
\tag{33}
\]

Combining (33) with (6) proves (10).

The estimate is deliberately one-sided. No asymptotic equivalence `T_n~log p_n` is needed, and extreme neighboring prime gaps cannot make the canonical cusp-entry length grow faster than the logarithmic budget already absorbed by (6).

## 5. Trace-level interpolation consequence and remaining gate

Let `chi:[0,1]->[0,1]` be any fixed smooth cutoff. On the finite Busemann interval `[0,T_n]`, a scalar transition

\[
k_n(\tau)=c_n\,\chi(\tau/T_n)
\tag{34}
\]

satisfies

\[
\|k_n\|_\infty\le|c_n|,
\qquad
\int_0^{T_n}|k_n(\tau)|\,d\tau
\le C T_n|c_n|,
\qquad
\int_0^{T_n}|k_n'(\tau)|\,d\tau
\le C|c_n|.
\tag{35}
\]

Equations (10) and PF-132's `sum |c_n|<infinity` therefore give a summable family of these one-dimensional scalar corrections. Together with PF-133's exponentially decaying centered tail and PF-129's fixed-slab synchronization followed by exact agreement in the deep cusp, this closes a specific boundary-trace concern:

\[
\boxed{
\text{growing pre-cusp length}
\times
\text{Lambert scalar mismatch}
\in\ell^1.
}
\tag{36}
\]

But (35) is **not** a two-dimensional extension theorem. A cutoff that varies transversely across a narrowing cusp or collar can acquire additional orthonormal-frame derivatives, and the Güneysu--Thalmaier criterion weights metric deviation by inverse unit-ball volume. PF-134 therefore does not combine PF-129, PF-130, PF-132, and PF-133 into a global wave-operator proof. The surviving accepted-clue gates remain boundary-coherent two-dimensional extension/gluing and control of all ambient thin regions, including noncanonical ones.

## 6. Prior art and novelty audit

No novelty is claimed for discrete summation by parts, Bertrand's postulate, the Baker--Harman--Pintz prime-gap bound, Lambert quadrilateral geometry, Busemann coordinates, or cutoff interpolation. The external operator target also remains standard: Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, gives an integral criterion for existence and completeness of wave operators for quasi-isometric complete metrics without an injectivity-radius lower bound. PF-134 does not satisfy or extend that theorem; it only removes one concrete project-local summability obstruction before the metric-level criterion can even be tested.

Directed searches for hyperbolic flute metric perturbations, Lambert-quadrilateral boundary traces, and wave-operator criteria found no literature statement matching the exact prime/shift-clone estimate (6) or its canonical cusp-entry consequence (10). Absence of matching wording is not a novelty claim. The durable Mathia contribution is the narrow combination of already-established exact geometry and arithmetic control:

\[
\boxed{
\text{shift mesh first difference}
\ +\ 
\text{collar regular remainder}
\ +\ 
\text{Lambert parameter correction}
\Longrightarrow
\sum_n (\log p_n)|c_n|<\infty.
}
\tag{37}
\]

This is a **negative/boundary result** for the all-composite shift control: a logarithmically growing cusp-entry distance cannot amplify the surviving scalar trace mode into a divergence, so any failure of the accepted wave-operator clue must arise at the genuine two-dimensional/global operator gates rather than from this one-dimensional propagation length.

## 7. Audit / falsification core

A later adversary can check PF-134 through the following finite chain:

1. import PF-114's monotonicity `d_n increasing to 0` and asymptotic `d_n=-1/p_n+o(1/p_n)`; apply (13)--(15) to prove the log-weighted variation (16);
2. import PF-119's exact decomposition `epsilon_n=-d_n+r_n` with `r_n=E(h_n^+)-E(h_n)` and `E(h)=h^2/12+O(h^4)`;
3. use PF-114's `h_n \ll g_n/p_n` and Baker--Harman--Pintz `g_n\ll p_n^{0.525}` to verify (20), then compare the weighted prime-interval sum with the convergent integral in (21);
4. import PF-132's exact `s_n=beta_n-epsilon_n` and exponential large-cuff bound (25), then use the collar identity (26) to prove (27) and hence (6);
5. verify PF-119's split-foot height (7); use only `sin u<=u`, the minimum odd-prime gap `g_n>=2`, and Bertrand twice to prove (33);
6. combine (6) and (33) to obtain (10), and verify the elementary cutoff estimates (35);
7. do **not** promote the trace-level cutoff to a metric deformation without bounding all longitudinal/transverse derivatives, density change, quasi-isometry constants, and the inverse-unit-ball-volume weight globally.

A refutation would need to break one of the imported exact identities/asymptotics or the weighted summation estimates. Failure to construct the two-dimensional extension would not refute PF-134; it would locate the still-open operator-level obstruction exactly where this finding leaves it.