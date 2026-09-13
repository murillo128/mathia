# MC-271 — Positive shell generating majorants cannot cross the blind-atom threshold

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the flat Christoffel shell matrix from `MC-269` and `MC-270`. Write

\[
\mathcal B_m=\{S\subseteq\mathcal P_y:|S|\le m\},
\qquad Z=|\mathcal B_m|,
\]

and let

\[
N=N_y=|\mathcal R_y|.
\]

For every target subset `T\subseteq\mathcal R_y`, put

\[
g(T):=\sum_{S\in\mathcal B_m}\chi_T(q_S),
\]

and group the flat energies by target-shell weight:

\[
F_j:=\sum_{\substack{T\subseteq\mathcal R_y\\|T|=j}}|g(T)|^2,
\qquad 0\le j\le N.
\tag{1}
\]

Thus the live quantity in `MC-270` is `F_t`, and a blind target row of weight `t` contributes exactly `Z^2` to `F_t`.

A natural way to keep the flat source vector while avoiding a fixed-shell estimate is to form the nonnegative ordinary generating polynomial

\[
G(z):=\sum_{j=0}^{N}F_j z^j
\tag{2}
\]

and use, for real `z>0`, the standard coefficient majorant

\[
F_t\le z^{-t}G(z).
\tag{3}
\]

This route cannot exclude even one blind row in the live regime. More precisely, let

\[
d_*:=\max\{j:F_j>0\}.
\]

Then the sparse source support forces

\[
\boxed{
d_*\ge N-\log_2 Z.
}
\tag{4}
\]

Moreover Parseval gives

\[
\boxed{
G(1)\ge 2^N Z.
}
\tag{5}
\]

Consequently, for every `z>0`, the positive-real coefficient bound `(3)` is too large to prove the strict inequality `F_t<Z^2` required for blind exclusion. For `0<z\le1`, already

\[
z^{-t}G(z)\ge z^{-t}F_0=z^{-t}Z^2\ge Z^2.
\tag{6}
\]

For `z\ge1`, `(4)` and `(5)` give

\[
\frac{z^{-t}G(z)}{Z^2}
\ge
\max\left\{
\frac{2^N}{Zz^t},
\frac{z^{d_*-t}}{Z^2}
\right\}.
\tag{7}
\]

If `d_*>t`, the two lower bounds in `(7)` are respectively decreasing and increasing in `z`; their crossing occurs at

\[
z_c=(2^N Z)^{1/d_*}.
\tag{8}
\]

Hence

\[
\boxed{
\inf_{z\ge1}
\frac{z^{-t}G(z)}{Z^2}
\ge
\frac{2^N}{Z}(2^NZ)^{-t/d_*}.
}
\tag{9}
\]

At the live choice

\[
m=t+1,
\qquad t\asymp\log\log y,
\qquad k_y,N_y\asymp\frac y{\log y},
\]

one has

\[
\log Z=o(N),
\qquad t=o(N),
\qquad d_*=N-o(N).
\tag{10}
\]

Therefore the right-hand side of `(9)` is

\[
\boxed{
\exp\big((\log 2-o(1))N\big),
}
\tag{11}
\]

not merely slightly above the blind threshold.

Thus **positive shell Poissonization does not provide an escape from `MC-270`**. Keeping the flat source vector but replacing the fixed target shell by a positive generating function destroys too much shell localization: low positive fugacity is blocked by the unavoidable weight-zero coefficient, while high positive fugacity is blocked by the combination of total Walsh energy and a forced Fourier coefficient at weight `N-o(N)`.

The live theorem must therefore retain signed fixed-shell information, or introduce genuinely new information before coefficient extraction. No blind row is excluded here and no bound for `M(X)` follows.

## 1. The shell polynomial is the Walsh-energy profile of a sparse syndrome measure

For each source subset `S\in\mathcal B_m`, define its upper-prime Legendre syndrome

\[
\Phi(S)\in\mathbb F_2^N
\]

by

\[
(-1)^{\Phi(S)_r}
=\left(\frac{q_S}{r}\right)
\qquad(r\in\mathcal R_y).
\tag{12}
\]

Let

\[
\nu(x):=\#\{S\in\mathcal B_m:\Phi(S)=x\},
\qquad x\in\mathbb F_2^N.
\tag{13}
\]

Then `\nu` is a nonnegative integer-valued function satisfying

\[
\sum_x\nu(x)=Z,
\qquad
|\operatorname{supp}\nu|\le Z.
\tag{14}
\]

For a target subset `T`, identified with its indicator vector in `\mathbb F_2^N`,

\[
g(T)
=\sum_x\nu(x)(-1)^{T\cdot x}.
\tag{15}
\]

So `g` is exactly the unnormalized Walsh transform of the syndrome multiplicity function `\nu`, and `(1)` is its Fourier energy grouped by Hamming weight.

This representation uses the actual arithmetic syndromes. Collisions `\Phi(S)=\Phi(U)` only shrink `|supp\nu|` and therefore strengthen the support argument below.

## 2. Sparse support forces a Fourier coefficient near the top shell

The only structural input needed for `(4)` is the classical degree-versus-support bound on the Boolean cube:

> If a nonzero function on `\{\pm1\}^N` has Fourier degree at most `d`, then it is nonzero on at least `2^{N-d}` cube points.

For completeness, this has a short induction. Write a nonzero multilinear polynomial of degree at most `d` as

\[
f(x_1,\dots,x_N)
=x_N h(x_1,\dots,x_{N-1})+q(x_1,\dots,x_{N-1}),
\]

choosing a coordinate in a highest-degree monomial so that `h` is nonzero and has degree at most `d-1`. Whenever `h` is nonzero at a point of the `(N-1)`-cube, the two values of `f` obtained from `x_N=\pm1` differ by `2h`, so at least one is nonzero. Induction gives at least

\[
2^{(N-1)-(d-1)}=2^{N-d}
\]

nonzero values.

Apply this to `\nu`. By Walsh inversion, its Fourier degree is exactly

\[
d_*:=\max\{|T|:g(T)\ne0\}.
\]

Since `\nu` is nonzero and has support at most `Z`,

\[
2^{N-d_*}
\le|\operatorname{supp}\nu|
\le Z,
\]

which proves `(4)`.

This is the familiar minimum-distance phenomenon behind Reed--Muller codes: degree-`d` Boolean polynomials have minimum nonzero support `2^{N-d}`. No novelty is claimed for that theorem. A current coding-theory reference recording the equivalent Reed--Muller minimum-distance formula is the Error Correction Zoo entry `Reed-Muller (RM) code`, https://errorcorrectionzoo.org/c/reed_muller; classical Reed--Muller theory is the prior-art boundary.

The Mathia-specific consequence is that the very sparse arithmetic syndrome measure cannot have all of its Walsh energy confined to low target-shell weights. Some shell at distance at most `\log_2 Z` from the top must contain a nonzero coefficient.

## 3. Parseval supplies exponentially large total shell energy

Walsh Parseval applied to `(15)` gives

\[
\sum_{T\subseteq\mathcal R_y}|g(T)|^2
=2^N\sum_{x\in\mathbb F_2^N}\nu(x)^2.
\tag{16}
\]

The left-hand side is exactly `G(1)`. Because `\nu(x)` is a nonnegative integer,

\[
\nu(x)^2\ge\nu(x),
\]

and hence

\[
G(1)
=2^N\sum_x\nu(x)^2
\ge2^N\sum_x\nu(x)
=2^NZ,
\]

which proves `(5)`.

Equality holds exactly when the syndrome map is injective on `\mathcal B_m`. Source collisions increase the total energy and therefore do not help the positive-generating-function route.

## 4. Why every positive real fugacity misses the blind threshold

The coefficient inequality `(3)` is elementary because every `F_j` is nonnegative.

For `0<z\le1`, the constant shell is already fatal:

\[
F_0=|g(\varnothing)|^2=Z^2.
\]

This proves `(6)`. In particular, the usual subunit saddle used to localize low binomial degrees cannot possibly certify `F_t<Z^2` without first removing or cancelling lower shells.

For `z\ge1`, coefficientwise monotonicity gives

\[
G(z)\ge G(1)\ge2^NZ,
\]

while the top occupied shell from `(4)` gives

\[
G(z)\ge F_{d_*}z^{d_*}\ge z^{d_*},
\]

because `g(T)` is an integer and a nonzero term has `|g(T)|^2\ge1`. Dividing by `z^tZ^2` yields `(7)`.

When `d_*>t`, minimizing the maximum of the decreasing first term and increasing second term places the optimum at their crossing `(8)`, giving `(9)`.

Now set

\[
\alpha_N:=\frac{\log Z}{N\log2}.
\]

Then `(4)` implies

\[
\frac{d_*}{N}\ge1-\alpha_N.
\tag{17}
\]

At the live scales, `\alpha_N=o(1)` and `t/N=o(1)`. Taking logarithms in `(9)` gives

\[
\log\left[
\frac{2^N}{Z}(2^NZ)^{-t/d_*}
\right]
=N\log2-\log Z
-\frac{t}{d_*}(N\log2+\log Z)
=(\log2-o(1))N,
\]

which proves `(11)`.

The obstruction is therefore much stronger on the superunit side than a failure to gain the final factor `Z/C`: the best lower certificate available from these unavoidable coefficients is exponentially above one blind atom after normalization by `Z^2`.

## 5. Prior art and novelty boundary

The Walsh transform, Parseval identity, nonnegative coefficient majorant `a_t\le z^{-t}\sum_j a_jz^j`, and the degree/support theorem are classical. The latter is the minimum-distance theorem for Reed--Muller evaluation codes in equivalent language. No novelty is claimed for any of them.

The Krawtchouk shell language used in the immediately preceding findings is also classical. NIST DLMF §18.23.3 records the standard Krawtchouk generating function, https://dlmf.nist.gov/18.23#E3, while MacWilliams weight-enumerator transforms are classical coding theory; see https://encyclopediaofmath.org/wiki/MacWilliams_identities. These sources delimit the representation-level prior art rather than support a novelty claim.

A targeted literature search through 13 September 2026 did not identify this exact combination applied to the Mathia sparse Legendre-syndrome / Christoffel flat-energy object. That absence is not evidence of novelty. The durable delta is the exact frontier consequence: after `MC-270` rules out coefficient-uniform operator norms, **positive radialization over target-shell degree is also incapable of crossing the same blind atom even though it keeps the flat source coefficients**.

## 6. Boundaries and updated frontier

- The finding blocks the unmodified positive-real generating polynomial `(2)` together with the one-point coefficient majorant `(3)`. It does **not** block direct estimates of `F_t`.
- Complex Cauchy-integral extraction can exploit phase cancellation and is not covered. Neither are signed kernels, alternating shell combinations, or other transforms whose coefficients are not all nonnegative.
- Subtracting known lower or upper shell coefficients before applying a positive majorant is also not covered; doing so requires additional shell-specific information, which is precisely what the raw positive generating function lacks.
- The degree/support argument is insensitive to quadratic reciprocity and prime localization. It is a structural obstruction caused by the sparse source syndrome measure itself.
- `(4)` does not say that the high occupied shell is large; only that some coefficient there is nonzero. Integrality is enough because superunit fugacity amplifies any such coefficient.
- No statement is made about the actual size of `F_t`, and no arithmetic pseudorandomness theorem is proved.

Together with `MC-269` and `MC-270`, the flat-energy frontier is now sharper. Absolute-value control of radial source layers loses impossible precision; coefficient-uniform operator norms meet the blind atom exactly; and positive shell generating majorants cannot isolate the target shell at all. The remaining viable route is genuinely **fixed-weight signed cancellation** in

\[
F_t-CZ
=\sum_{S\ne U}K_t(d(S\triangle U);N),
\]

or an arithmetic transform that preserves equivalent signed shell information instead of replacing it by positive radial smoothing.