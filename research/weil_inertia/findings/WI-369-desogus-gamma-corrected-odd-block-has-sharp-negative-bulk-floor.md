# WI-369 — Desogus's gamma-corrected odd block has a sharp negative bulk floor

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + SHARP-SEMIBOUND + DECISIVE-REPAIR-BARRIER + NON-ESTABLISHED-RH`.

## Claim

The exact gamma-corrected odd archimedean block obtained in WI-364 from Marco Desogus's 17 September 2026 preprint **The Three Gates: A Rooted-Operator Approach to Weil Positivity** (`arXiv:2609.20367v1`) admits a complete form decomposition on the common test core `C_c^1(0,1)`. After the singular Cauchy channel, endpoint potential, scalar normalization and the full regular gamma image are combined with the correct signs, all `A`-dependent scalar and logarithmic terms cancel and one obtains

\[
\boxed{
\mathcal A_A[f]+C_\Gamma\|f\|_2^2
=
\frac A2\iint_{(0,1)^2}h(A|u-v|)|f(u)-f(v)|^2\,du\,dv
+
\int_0^1\!\bigl(H(Au)+H(A(1-u))\bigr)|f(u)|^2\,du
+
A\iint_{(0,1)^2}h(A(u+v))f(u)\overline{f(v)}\,du\,dv,
}
\tag{1}
\]

where

\[
h(s)=\frac{e^{-s/2}}{1-e^{-2s}},
\qquad
H(z)=\operatorname{artanh}(e^{-z/2})+\arctan(e^{-z/2}),
\tag{2}
\]

and

\[
\boxed{
C_\Gamma=\frac\pi2+\gamma+\log(8\pi)
=5.3721834192256655822\ldots .
}
\tag{3}
\]

Every term on the right of (1) is nonnegative. Consequently

\[
\boxed{\mathcal A_A\ge -C_\Gamma I}
\tag{4}
\]

as a quadratic-form inequality on this core.

The constant is not merely a convenient lower bound. It is **asymptotically sharp in the bulk**. Define the form bottom on the common core by

\[
\lambda_A:=
\inf_{0\ne f\in C_c^1(0,1)}
\frac{\mathcal A_A[f]}{\|f\|_2^2}.
\tag{5}
\]

Then

\[
\boxed{\lim_{A\to\infty}\lambda_A=-C_\Gamma.}
\tag{6}
\]

Thus the repaired gamma-corrected archimedean collar does **not** possess a positive uniform OSPR/Schur reserve by itself in the cofinal large-`A` regime. WI-366 already ruled out obtaining such a reserve by uniformly comparing the true image channel with a fixed bare Carleman operator. Equation (6) is stronger: the *entire corrected odd archimedean block* has a fixed negative bulk floor, and fixed interior test functions asymptotically attain it.

This is a barrier to a repair mechanism, not to the full Weil operator and not to RH. A viable rooted/Schur induction may still work if the arithmetic/source/polar channels supply at least this fixed debit on the source-conditioned subspaces actually used by the induction. What is ruled out is treating the corrected archimedean collar alone as an asymptotically positive source of uniform reserve.

## 1. Exact normalized form under audit

WI-364 reconstructed the odd fold of the localized archimedean part of `arXiv:2609.20367v1`. After pairing the singular Carleman image with its regular gamma image, write the resulting normalized form as

\[
\mathcal A_A[f]
=
\mathfrak b[f]+c_0(A)\|f\|_2^2
-A\iint\rho(A|u-v|)f(u)\overline{f(v)}\,du\,dv
+\langle f,J_Af\rangle,
\tag{7}
\]

where

\[
\mathfrak b[f]
=
\frac14\iint\frac{|f(u)-f(v)|^2}{|u-v|}\,du\,dv
-
\frac12\int_0^1\log(u(1-u))|f(u)|^2\,du,
\tag{8}
\]

\[
\rho(s)=h(s)-\frac1{2s},
\qquad
c_0(A)=-\log A-\log(2\pi)-\gamma,
\tag{9}
\]

and the true positive image channel is

\[
J_A(u,v)=Ah(A(u+v)).
\tag{10}
\]

Equation (10) is exactly the combination

\[
\frac1{2(u+v)}+A\rho(A(u+v))=Ah(A(u+v))
\tag{11}
\]

forced by the odd fold. This is the channel isolated in WI-364--WI-366, rather than the bare Carleman term used in the printed cancellation argument.

The calculation below is first a quadratic-form identity on `C_c^1(0,1)`. No claim about a particular self-adjoint closure or operator-domain realization is needed for the semibound or the sharpness test.

## 2. The regular difference kernel has an exact primitive

For the symmetric kernel

\[
k_A(u,v)=A\rho(A|u-v|),
\tag{12}
\]

the standard graph identity gives

\[
-\iint k_A(u,v)f(u)\overline{f(v)}\,du\,dv
=
-\int_0^1 r_A(u)|f(u)|^2\,du
+
\frac12\iint k_A(u,v)|f(u)-f(v)|^2\,du\,dv,
\tag{13}
\]

with

\[
r_A(u)
=
\int_0^{Au}\rho(s)\,ds
+
\int_0^{A(1-u)}\rho(s)\,ds.
\tag{14}
\]

The needed primitive can be evaluated in closed form. Since, with `t=e^{-s/2}`,

\[
\int_z^\infty h(s)\,ds
=
2\int_0^{e^{-z/2}}\frac{dt}{1-t^4}
=
\operatorname{artanh}(e^{-z/2})+\arctan(e^{-z/2})
=:H(z),
\tag{15}
\]

we have `H'(z)=-h(z)`. Moreover

\[
H(z)=\log2-\frac12\log z+\frac\pi4+o(1)
\qquad(z\downarrow0).
\tag{16}
\]

Therefore the primitive normalized by `I(0)=0` is

\[
\boxed{
I(z):=\int_0^z\rho(s)\,ds
=
\log2+\frac\pi4-rac12\log z-H(z).
}
\tag{17}
\]

In particular

\[
r_A(u)
=
2\log2+\frac\pi2
-\log A
-rac12\log(u(1-u))
-H(Au)-H(A(1-u)).
\tag{18}
\]

## 3. All scalar and endpoint logarithms cancel exactly

Insert (13) and (18) into (7). The difference part in (8) combines with the second term in (13) through

\[
\frac1r+2A\rho(Ar)=2Ah(Ar),
\tag{19}
\]

so their sum is

\[
\frac A2\iint h(A|u-v|)|f(u)-f(v)|^2\,du\,dv.
\tag{20}
\]

At the diagonal level, `-r_A(u)` contributes

\[
-2\log2-\frac\pi2
+\log A
+rac12\log(u(1-u))
+H(Au)+H(A(1-u)).
\tag{21}
\]

The `+\frac12\log(u(1-u))` term cancels the endpoint potential in (8), while `+\log A` cancels the scale term in `c_0(A)`. The remaining scalar is

\[
-2\log2-\frac\pi2-\log(2\pi)-\gamma
=-\left(\frac\pi2+\gamma+\log(8\pi)\right).
\tag{22}
\]

Together with the unchanged image channel (10), this proves the exact identity (1).

## 4. The remainder in (1) is manifestly nonnegative

The first term of (1) is nonnegative because `h(s)>0` for `s>0`. The second is nonnegative because `H(z)>0` for `z>0`.

For the image term, the geometric-series expansion

\[
\boxed{
h(s)=\sum_{n\ge0}e^{-(2n+1/2)s}}
\tag{23}
\]

shows directly that

\[
Ah(A(u+v))
=
A\sum_{n\ge0}
 e^{-A(2n+1/2)u}
 e^{-A(2n+1/2)v}
\tag{24}
\]

is a positive-semidefinite Hankel kernel. Hence every term on the right of (1) is nonnegative, proving (4).

Notice the structural content of (1): the sign problem is no longer hidden in a singular Cauchy-versus-gamma cancellation. After exact bookkeeping, the corrected collar is a fixed negative scalar `-C_Gamma I` plus three explicitly positive pieces: a screened difference form, a positive endpoint multiplier and a positive Hankel image.

## 5. Bulk test functions make every positive remainder vanish

Fix any nonzero `f\in C_c^1(0,1)` with support contained in `[\delta,1-\delta]` for some `\delta>0`. Let `L=\|f'\|_\infty`.

For the screened difference term, `|f(u)-f(v)|\le L|u-v|`, so

\[
\begin{aligned}
0&\le
\frac A2\iint h(A|u-v|)|f(u)-f(v)|^2\,du\,dv\\
&\le
\frac{L^2}{A^2}\int_0^\infty s^2h(s)\,ds.
\end{aligned}
\tag{25}
\]

The last moment is finite and can itself be evaluated exactly. From (23),

\[
\int_0^\infty s^2h(s)\,ds
=
16\sum_{n\ge0}\frac1{(4n+1)^3}
=
\boxed{7\zeta(3)+\frac{\pi^3}{4}}.
\tag{26}
\]

Thus (25) is `O(A^{-2})`.

On the support of `f`, both `Au` and `A(1-u)` are at least `A\delta`, and (15) gives

\[
H(Au)+H(A(1-u))=O(e^{-A\delta/2})
\tag{27}
\]

uniformly there. The endpoint term in (1) therefore tends to zero.

Likewise `u+v\ge2\delta` on the support, so

\[
0\le
\langle f,J_Af\rangle
\le
\frac{Ae^{-A\delta}}{1-e^{-4A\delta}}\,\|f\|_1^2
\longrightarrow0.
\tag{28}
\]

Combining (1), (25), (27) and (28) gives

\[
\frac{\mathcal A_A[f]}{\|f\|_2^2}
\longrightarrow -C_\Gamma.
\tag{29}
\]

The lower bound (4) gives `\lambda_A\ge-C_\Gamma` for every `A`, while (29), using this one fixed admissible test function in the infimum (5), gives `\limsup_A\lambda_A\le-C_\Gamma`. This proves (6).

## 6. Consequence for the Desogus repair tree

WI-364 showed that the paper's printed Cauchy--gamma cancellation omits the parity image channel. WI-365 established that the omitted true image is favorable in sign. WI-366 then showed that this image cannot uniformly dominate a fixed copy of the bare Carleman operator, and WI-368 identified the opposite off-diagonal sign that prevents the proposed positive-kernel scalar cancellation from closing the repaired form.

Equation (1) resolves the remaining archimedean-only question more sharply. The corrected collar does have a clean lower bound, but its cofinal bulk floor is

\[
-C_\Gamma=-5.372183419225\ldots,
\tag{30}
\]

not a positive constant. Because fixed interior test functions asymptotically kill **all three** positive remainders, no strengthening that uses only these archimedean terms can turn (4) into a uniform positive reserve on the full normalized test core.

Therefore the next viable test is source-conditioned rather than archimedean-only: write the exact Schur/root form including the arithmetic square/source terms and ask whether those terms uniformly finance the debit `C_Gamma` on the subspace actually reached by the source map. Equivalently, a repaired induction must prove that its active source geometry cannot approximate the bulk quasimodes used in (29), or must add a genuinely nonlocal positive channel not present in (1).

This is directly relevant to the `weil_inertia` mandate because it identifies an exact quantitative defect in a contemporary claimed positivity route and replaces an ambiguous `missing positive reserve` question by a concrete coercivity target. It does **not** transfer any unproved RH claim from the preprint into this line.

## 7. Provenance and novelty audit

**Primary source under audit.** Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, arXiv:2609.20367v1, submitted 17 September 2026. The load-bearing inputs here are the localized odd operator, `c_0(A)`, the regular gamma kernel `rho`, the odd parity reduction and the Cauchy--gamma transport used around Lemmas 5.1--5.2 and Proposition 5.3. As checked during this research pass on 20 September 2026, the arXiv record remained at version 1.

**Internal exact dependencies.** WI-364 supplies the source-exact odd fold and the forced gamma image; WI-365 records positivity of the true image; WI-366 gives the earlier no-uniform-Carleman-domination barrier; WI-367 fixes the complete Cauchy--Carleman half-density transport; WI-368 records the sign mismatch in the attempted positive-kernel cancellation. No statement from another Mathia research line is promoted from read-only evidence here.

**Novelty audit.** The primitive (15)--(17), geometric expansion (23), and graph-form identity (13) are elementary/classical ingredients. A targeted audit of the Desogus preprint and the immediately relevant Mathia/source trail did not locate a separate statement of the exact decomposition (1), the universal constant (3), or the asymptotically sharp form-bottom limit (6). This is recorded only as a prior-art audit result, **not** as a claim of priority.

## Research consequence

The archimedean repair branch is now quantitatively pinned down: after exact gamma-image bookkeeping, its best uniform full-core statement is a sharp negative floor. The open bootstrap question is therefore no longer whether the corrected collar is secretly positive. It is whether the arithmetic/source-conditioned Schur geometry supplies a uniform surplus of at least `C_Gamma`, or excludes the interior bulk quasimodes that make the archimedean lower bound sharp.
