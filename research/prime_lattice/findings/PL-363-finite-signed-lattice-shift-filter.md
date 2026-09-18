# PL-363 — Finite signed lattice-shift filters move ordinary zeta convergence to `Re(s)>0` but do not single out `1/2`

**Evidence:** `EXACT-DERIVED + CLASSICAL-DIRICHLET-SERIES-CONTROL + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-362`.

**Status:** `FINITE-POLE-CANCELLING-LATTICE-SHIFTS-CREATE-A-CONDITIONAL-CONVERGENCE-STRIP-BUT-NO-RH-LOCALIZATION-MECHANISM`.

## Precise claim

`PL-362` proves that coefficientwise-positive approximate identities cannot cross zeta's ordinary convergence wall at `Re(s)=1`. The most elementary escape is to allow a finite sign-indefinite combination of multiplicative lattice shifts. That escape does cross the wall, but only in a completely classical and rigid way.

Let

\[
S_m e_n=e_{mn},
\qquad
v(mn)=v(m)+v(n),
\tag{PL363-1}
\]

and let

\[
T=\sum_{m\in F}c_mS_m
\tag{PL363-2}
\]

for a finite set `F subset N` and coefficients `c_m in C`. Apply `T` formally to the coefficient-one zeta vector `Omega=sum_{n>=1}e_n`. The coefficient at `e_k` is

\[
b_k=\sum_{\substack{m\in F\\m\mid k}}c_m.
\tag{PL363-3}
\]

Write

\[
P(s)=\sum_{m\in F}c_m m^{-s}.
\tag{PL363-4}
\]

Then, initially only in the absolutely convergent half-plane `Re(s)>1`,

\[
\sum_{k\ge1}b_k k^{-s}=P(s)\zeta(s).
\tag{PL363-5}
\]

If `M=lcm(F)`, the sequence `(b_k)` is periodic modulo `M`, and its period mean is

\[
\frac1M\sum_{r=1}^M b_r
=
\sum_{m\in F}\frac{c_m}{m}
=
P(1).
\tag{PL363-6}
\]

Consequently the exact pole-cancellation condition

\[
P(1)=0
\tag{PL363-7}
\]

is equivalent to zero mean of the periodic output coefficients. Under (PL363-7), the partial sums of `(b_k)` are bounded, so Dirichlet/Abel summation gives ordinary locally uniform convergence of

\[
B(s):=\sum_{k\ge1}b_k k^{-s}
\tag{PL363-8}
\]

throughout

\[
\boxed{\operatorname{Re}s>0.}
\tag{PL363-9}
\]

If `T` is nonzero, then `(b_k)` is nonzero by Möbius inversion. Periodicity then gives a subsequence on which `|b_k|` is a fixed positive number, so the terms in (PL363-8) fail to tend to zero at every point with `Re(s)<=0`. Thus the ordinary convergence half-plane in the pole-cancelling nontrivial case is sharp:

\[
\boxed{\sigma_c(B)=0.}
\tag{PL363-10}
\]

Moreover `|b_k|` is a nonzero periodic sequence, hence has positive period mean, so

\[
\boxed{\sigma_a(B)=1.}
\tag{PL363-11}
\]

The finite signed lattice filter therefore creates the full conditional strip `0<Re(s)<=1`, but there is no transition at `Re(s)=1/2`.

## 1. One-prime filter: Dirichlet eta as a lattice finite difference

The canonical one-coordinate example is

\[
T_p=I-pS_p.
\tag{PL363-12}
\]

Because `S_p` translates the exponent vector by the prime basis direction `e_p`, its output coefficients are

\[
b_n=1-p\,\mathbf 1_{p\mid n}
=1-p\,\mathbf 1_{v_p(n)\ge1}.
\tag{PL363-13}
\]

The period mean is zero, and for `Re(s)>1`,

\[
B_p(s)
=
\sum_{n\ge1}(1-p\mathbf 1_{p\mid n})n^{-s}
=
(1-p^{1-s})\zeta(s).
\tag{PL363-14}
\]

For `p=2`, (PL363-13) is `(-1)^{n-1}` and (PL363-14) is exactly the classical Dirichlet eta identity

\[
\eta(s)=(1-2^{1-s})\zeta(s),
\tag{PL363-15}
\]

whose defining Dirichlet series converges for `Re(s)>0`. NIST DLMF §25.11.8 gives the corresponding alternating Hurwitz-zeta series representation in this half-plane, while DLMF §25.2 records that the coefficient-one zeta series itself is valid only for `Re(s)>1` and that zeta is continued meromorphically elsewhere.

For every prime `p`, the zeros of the elementary factor satisfy

\[
1-p^{1-s}=0
\quad\Longleftrightarrow\quad
s=1-\frac{2\pi i k}{\log p},\qquad k\in\mathbb Z,
\tag{PL363-16}
\]

so they all lie on `Re(s)=1`. Hence throughout the open critical strip `0<Re(s)<1`, the factor in (PL363-14) is nonzero. The one-prime filter transports exactly the zeta zero divisor there; it does not constrain that divisor to `Re(s)=1/2`.

## 2. Periodic coefficients give the complete continuation mechanism

The continuation furnished by a finite filter can be described without pretending that (PL363-5) was initially valid in the critical strip. Periodicity gives, first for `Re(s)>1`,

\[
B(s)
=
M^{-s}\sum_{r=1}^{M}b_r\,\zeta\!\left(s,\frac rM\right).
\tag{PL363-17}
\]

NIST DLMF §25.11 states that each Hurwitz zeta function is meromorphic on the whole `s`-plane with only a simple pole at `s=1`, of residue `1`. The residue of the right side of (PL363-17) is therefore proportional to `sum_{r=1}^M b_r`, which vanishes exactly under (PL363-7). Thus a pole-cancelling finite lattice filter has an **entire** continuation.

This does not mean that the ordinary series (PL363-8) converges everywhere. The distinction is exact:

\[
\text{ordinary convergence: }\operatorname{Re}s>0,
\qquad
\text{analytic continuation: all }s\in\mathbb C.
\tag{PL363-18}
\]

Combining (PL363-5) with analytic continuation gives

\[
B(s)=P(s)\zeta(s)
\tag{PL363-19}
\]

as an entire identity after the pole at `1` has been cancelled. Outside `Re(s)>1`, (PL363-19) is an analytic-continuation statement, not an Euler-product or coefficientwise identity justified by absolute convergence.

## 3. Why this does not produce RH rigidity

The finite-filter mechanism is too algebraically small to localize zeta zeros. Every such output has the form

\[
B=P\zeta
\tag{PL363-20}
\]

with `P` a finite exponential Dirichlet polynomial. The filter can cancel the pole at `1`, can create additional zeros through `P`, and can replace positive coefficients by periodic signed/complex coefficients whose partial sums are bounded. It does not supply a self-adjoint operator, positivity criterion, functional-equation duality, trace formula, determinant identity, or any other structure forcing the inherited zeta zeros onto the critical line.

The location `Re(s)=1/2` is especially absent from the convergence geometry: after pole cancellation the exact ordinary/absolute abscissae are `0` and `1`, respectively, and the critical line simply lies halfway inside that classical conditional-convergence strip. Nothing in the finite-shift argument distinguishes it from any other vertical line in `0<Re(s)<1`.

This is the decisive boundary relative to `PL-362`. Allowing signs is genuinely enough to evade the positive-cone obstruction, so positivity was load-bearing there. But **finite multiplicative-shift cancellation only manufactures classical periodic Dirichlet-series continuation**. A future signed or complex renormalization candidate must therefore contain structure beyond a fixed finite combination of exponent-lattice translations if it is to carry RH-specific information.

## 4. Prior-art and novelty audit

No theorem-level novelty is claimed for the analytic facts. The `p=2` case is Dirichlet's eta function, one of the standard continuations of zeta. More generally, zero-mean periodic Dirichlet coefficients and their Hurwitz-zeta decomposition are classical. The authoritative controls used here are NIST DLMF §25.2 for the domain of the ordinary zeta Dirichlet series and meromorphic continuation, and NIST DLMF §25.11 for Hurwitz zeta, including its unique simple pole at `1` and the alternating series representation valid for `Re(s)>0`.

The durable delta is instead a **prime-lattice route restriction**. `PL-362` left signed/complex cancellation as an explicit escape from the positive-filter no-go result. The present calculation classifies the most immediate such escape—finite combinations of lattice translations—and shows both exactly how far ordinary convergence moves and exactly why this move supplies no critical-line localization. It therefore prevents a classical eta/periodic-series continuation from being mistaken for a new geometric RH mechanism.

## 5. Adversarial boundaries

1. **Finiteness is load-bearing.** An infinite or scale-dependent signed combination of prime shifts need not have periodic coefficients and is not covered by this finding. Such a construction may still be meaningful, but its convergence, continuation, and zero sensitivity must be audited independently.

2. **The pole-cancellation equation is exact.** If `P(1) != 0`, the periodic coefficient sequence has nonzero mean and its Dirichlet series retains ordinary abscissa of convergence `1`; there is no signed-filter gain of the type proved here.

3. **Continuation is not ordinary convergence.** The zero-mean series itself stops at `Re(s)=0`. Values farther left come from the Hurwitz-zeta/analytic continuation of the periodic Dirichlet series.

4. **General filters may add zeros.** Unlike the one-prime factor `1-p^{1-s}`, an arbitrary Dirichlet polynomial `P(s)` can have zeros inside the critical strip. Those are filter zeros, not evidence about the zeta divisor, and must not be conflated with inherited zeta zeros.

5. **No functional equation has been derived.** A filter can be chosen after knowing where zeta's pole is, and the condition `P(1)=0` merely removes that pole. The completed symmetry `s <-> 1-s` and the archimedean factor do not emerge from the finite exponent-lattice translation algebra.

6. **The result is not a no-go theorem for all signed renormalization.** It rules out only the fixed finite-shift family as an RH-localization mechanism. Infinite source-forced counterterms, target-relative constructions, nonlocal mixing, or structures tied independently to the functional equation remain outside its scope.

## Research consequence

The first explicit escape from `PL-362` is therefore understood completely. Finite sign-indefinite translations can cross `Re(s)=1`, but they do so by producing classical periodic cancellation with sharp ordinary boundary `Re(s)=0`; their analytic continuation is `P(s)zeta(s)` and carries no mechanism selecting `Re(s)=1/2`.

The next viable signed/complex candidate should not be another finite lattice filter. It must explain why its cancellation is globally forced—rather than chosen merely to annihilate the pole—and must retain a zero-sensitive structure that survives after the known analytic continuation has been factored out.