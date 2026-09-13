# VIS-203 — autocorrelation tapers make exact difference-shell coupling noncancelling

## Claim

Keep the finite-start prime-ratio polynomial of `VIS-192`--`VIS-194`,

`F_(y,H)(T)=sum_(lambda in Lambda_y) c_lambda exp(i lambda T)`,

with

`Lambda_y={+/-log(q/p): p<q<=y, p,q prime}`

and

`sum_lambda |c_lambda|^2=R_v(y,H)`.

There is a broad admissible subclass of the endpoint-zero tapers used in those findings for which **all terms having the same exact frequency difference carry the same phase and add with nonnegative amplitude**.

Precisely, choose a real smooth function `g` of compact support in `(-1/4,1/4)` with `int g != 0`, put

`w(x)=int_R g(t) g(t+x) dt`,

and define on `[0,1]`

`v(u)=w(u-1/2)`.

Then `v` is real, smooth, supported away from the endpoints, `v(0)=v(1)=0`, and

`V=int_0^1 v(u)du=(int g)^2>0`.

Its normalized Fourier kernel has the exact form

`kappa_v(theta)=exp(i theta/2) rho(theta)`,

where

`rho(theta)=|g_hat(theta)|^2/|g_hat(0)|^2 >= 0`.

Consequently every prime-ratio coefficient can be written

`c_lambda=exp(i H lambda/2) b_lambda`,

with `b_lambda>=0` and `b_(-lambda)=b_lambda`.

For a finite start window of length `L`, write

`E_(v,L)(T0)=R_(v,L)(T0;y,H)-R_v(y,H)`.

Grouping the exact expansion by frequency difference `xi=lambda-mu` gives

`E_(v,L)(T0)`
` = sum_(xi!=0) B_xi sinc(L xi/2)`
`   exp(i xi [T0+(H+L)/2])`,

where

`B_xi=sum_(lambda-mu=xi) b_lambda b_mu >=0`,

`B_(-xi)=B_xi`, and `sinc(x)=sin(x)/x`.

Thus there is **no cancellation inside an exact difference shell**. All multiplicities of the arithmetic relation

`lambda-mu=xi`

reinforce the same shell amplitude `B_xi`; any cancellation that improves on an absolute fiberwise treatment must instead come from interference **between distinct `xi` shells**, from spreading/packing their mass, or from deliberately choosing a taper whose centered Fourier transform changes sign.

Moreover the long-start Cesaro energy of the finite-window error is exactly

`lim_(R->infinity) R^(-1) int_0^R |E_(v,L)(T0)|^2 dT0`
` = sum_(xi!=0) B_xi^2 sinc^2(L xi/2)`.

Hence a uniform relative estimate

`sup_T0 |E_(v,L)(T0)| = o(R_v(y,H))`

necessarily implies

`sum_(xi!=0) B_xi^2 sinc^2(L xi/2)=o(R_v(y,H)^2)`.

At the fixed normalized collision scale of `VIS-195`, `|xi|<=A b_y` with `b_y~2/y^2`. Therefore for any subquadratic window `L=o(y^2)`,

`sinc(L xi/2)=1+o_A(1)`

uniformly on those dangerous shells. The box window itself does not attenuate them. A subquadratic uniform dephasing theorem using this taper class must therefore prove a genuine shell-packing/energy estimate for the nonnegative `B_xi`; exact-shell sign cancellation is unavailable.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL CORRELATION/FOURIER FACTORIZATION + NEGATIVE/CONTROL FRONTIER + NO-NOVELTY-CLAIM`.

No bound on the shell energies `B_xi`, no improvement of the `VIS-202` square-root-log threshold, and no optimal lower bound on the finite-start horizon is claimed.

## 1. Autocorrelation gives an admissible taper with nonnegative centered spectrum

Let

`g_tilde(x)=g(-x)`.

Then `w=g*g_tilde` in the correlation convention above. Because `g` is smooth and supported strictly inside `(-1/4,1/4)`, `w` is smooth and supported strictly inside `(-1/2,1/2)`. Shifting by `1/2` therefore gives an admissible `C^2` taper on `[0,1]` that actually vanishes in neighborhoods of both endpoints.

The ordinary correlation theorem gives

`int_R w(x) exp(i theta x) dx = |g_hat(theta)|^2`.

After the shift,

`int_0^1 v(u) exp(i theta u) du`
` = exp(i theta/2) |g_hat(theta)|^2`.

At `theta=0`,

`V=|g_hat(0)|^2=(int g)^2>0`.

Dividing by `V` proves

`kappa_v(theta)=exp(i theta/2) rho(theta)`

with `rho(theta)>=0` and even.

This construction is intentionally broad: the claim does not depend on a single named window or a tuned polynomial profile. Any smooth compactly supported `g` with nonzero integral supplies such a taper.

## 2. Prime-ratio coefficients inherit one linear phase

For positive `lambda=log(q/p)`, `VIS-192` gives

`c_lambda=Q_y^(-1) p^(-alpha) q^(-alpha) kappa_v(H lambda)`.

With the autocorrelation taper,

`c_lambda`
` = exp(i H lambda/2)`
`   Q_y^(-1) p^(-alpha)q^(-alpha) rho(H lambda)`.

Define the final factor as `b_lambda`. It is nonnegative. The negative-frequency coefficient is the conjugate of the positive one, and because `rho` is even the same formula

`c_lambda=exp(i H lambda/2)b_lambda`

holds for every `lambda in Lambda_y`, with `b_(-lambda)=b_lambda>=0`.

Thus the taper contributes only a phase linear in the frequency plus a nonnegative amplitude. This is the exact property that removes any possibility of cancellation among representations of the same difference frequency.

## 3. Group the finite-start error before taking absolute values

The exact finite-window expansion used in `VIS-194` is

`R_(v,L)(T0;y,H)`
` = sum_lambda |c_lambda|^2`
`   + sum_(lambda!=mu) c_lambda conjugate(c_mu)`
`     exp(i(lambda-mu)(T0+L/2))`
`     sinc((lambda-mu)L/2)`.

Subtracting `R_v=sum|c_lambda|^2` and inserting the coefficient factorization gives

`c_lambda conjugate(c_mu)`
` = exp(iH(lambda-mu)/2)b_lambda b_mu`.

For a fixed exact difference

`xi=lambda-mu`,

all pairs therefore have the same complex phase. Summing the pair amplitudes first yields

`B_xi=sum_(lambda-mu=xi)b_lambda b_mu>=0`

and the displayed shell formula in the claim.

This identifies exactly what was hidden by the scalar fiberwise bounds leading to `VIS-202`. Coupling several determinant fibers that land on the **same exact phase difference** cannot create destructive interference for this taper class: the fibers accumulate positively into `B_xi`.

The only remaining signed mechanism is across distinct shell frequencies. That mechanism is genuinely different from improving a pointwise four-form sieve count or averaging its local factor.

## 4. Start averaging diagonalizes the shell frequencies, not the representations inside a shell

The shell expansion is a finite exponential polynomial in `T0`. Different nonzero `xi` values are distinct frequencies, so ordinary Cesaro orthogonality gives

`lim_(R->infinity) R^(-1) int_0^R |E_(v,L)(T0)|^2 dT0`
` = sum_(xi!=0) |B_xi sinc(Lxi/2)|^2`.

This is an exact identity. In particular, cancellation between distinct shells that may occur at one specially chosen start cannot disappear from the uniform problem by rhetoric: if a uniform bound holds, the shell `l^2` energy must satisfy the same bound.

For the dangerous fixed-`A` crowding region of `VIS-195`,

`|xi|<=A b_y`, `b_y=log(1+2/y^2)`.

If `L=o(y^2)`, then

`sup_(|xi|<=A b_y) |L xi| ->0`,

so

`sinc(Lxi/2)=1+o_A(1)`

uniformly there. Therefore the desired subquadratic observation scale cannot rely on the box multiplier itself suppressing the worst prime-ratio collisions. The unresolved resource is the distribution of the positive shell masses `B_xi`.

## Prior-art audit

The analytic ingredient is classical. The correlation theorem identifies the Fourier transform of an autocorrelation with the squared modulus of the original Fourier transform; in the stationary formulation this is the familiar Wiener--Khinchin principle. Standard treatments of positive-definite and compactly supported kernels likewise use autocorrelation/self-correlation to obtain a nonnegative spectrum. Holger Wendland, *Scattered Data Approximation*, Cambridge University Press (2005), Chapters 6 and 9, is a standard reference for positive-definite and compactly supported functions. Modern covariance-kernel constructions also explicitly use self-correlation because its transform is an absolute square and hence nonnegative.

The shell regrouping and Cesaro orthogonality are elementary finite Fourier analysis. No novelty is claimed for autocorrelation tapers, positive-definite compactly supported functions, the correlation theorem, Wiener--Khinchin, or Parseval/Cesaro orthogonality.

The Mathia-specific content is the consequence for the exact `VIS-192` prime-ratio coefficients and the `VIS-202` structural frontier: within a large admissible taper subclass, coupling equal determinant-phase shells before scalarization is provably noncancelling, so a successful escape from the dimension-four fiberwise threshold must exploit cross-shell packing/interference or a genuinely different taper/dephasing resource.

## Boundaries and falsification

This is a control theorem for a broad admissible taper subclass, not for every real endpoint-zero taper. A symmetric taper whose centered Fourier transform changes sign can have signed amplitudes inside a difference shell, and a nonsymmetric taper can carry more general phases.

Accordingly the finding does not prove that all pre-scalarization cancellation routes fail. It proves that **exact-shell multiplicity by itself is not an intrinsic arithmetic cancellation mechanism**: there are fully admissible smooth tapers for which every representation in the shell has identical phase and nonnegative amplitude.

The result also does not estimate how many different `xi` shells occur, how `B_xi` is distributed among them, or whether their finite-start cosine phases cancel uniformly or on average. Those are the next mathematical questions if this route is pursued.

Falsify the finding by finding an error in the autocorrelation Fourier identity, an admissibility failure of the constructed taper, a prime-ratio coefficient whose centered amplitude is negative, a pair with fixed `xi` carrying a different residual phase, or a failure of the grouped finite-window/Cesaro identities.

## Research consequence

`VIS-202` left several structural escape routes after scalar cutoff optimization was exhausted. The present control eliminates one overly optimistic interpretation of "couple fibers before scalarization": simply grouping all representations of the same exact phase difference cannot provide cancellation for autocorrelation tapers; it reinforces them.

The next coherent route is therefore sharper. Either estimate the **shell-packing energy**

`sum_(xi) B_xi^2`

at the fixed normalized determinant scale, exploit cancellation between genuinely distinct shell frequencies under the start variable, or deliberately study sign-changing centered tapers and prove that their shell signs correlate beneficially with the arithmetic fibers. Repeating the four-form pointwise majorant, or hoping that exact difference multiplicity cancels automatically, cannot address the remaining boundary.